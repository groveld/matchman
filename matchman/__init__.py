from flask import Flask, redirect, render_template, request

from matchman.database import get_connection


def create_app():
    app = Flask(__name__)

    @app.route("/", methods=["GET"])
    def index():
        return redirect("/competitions")

    @app.route("/competitions", methods=["GET"])
    def competitions_overview():
        query = """
        SELECT
            C.COMPETITIONID,
            C.TITLE AS COMPETITION,
            CAST(C.BEGINDATE AS DATE) AS COMPETITION_DATE,
            EXTRACT(YEAR FROM C.BEGINDATE) AS COMPETITION_YEAR,
            COUNT(DISTINCT p.PARTICIPANTID) AS PARTICIPANTS
        FROM
            COMPETITIONS C
            JOIN PARTICIPANTS p ON C.COMPETITIONID = p.COMPETITIONID
        GROUP BY
            C.COMPETITIONID,
            C.BEGINDATE,
            C.TITLE
        ORDER BY
            C.BEGINDATE DESC
        """

        connection = get_connection()
        cursor = connection.cursor()
        cursor.execute(query)
        columns = [desc[0] for desc in cursor.description]
        competitions = [dict(zip(columns, row)) for row in cursor.fetchall()]
        cursor.close()
        connection.close()

        return render_template("competitions.html", competitions=competitions)

    @app.route("/competition/<int:competition_id>", methods=["GET"])
    def get_results(competition_id):
        view = request.args.get("view", "competition")  # Default view is "competition"

        query = (
            """
        SELECT
            co.TITLE AS COMPETITION,
            ca.DESCRIPTION AS CLASS,
            p.FIRSTNAME,
            p.LASTNAME,
            c.CLUBNAME,
            SUM(s.INNERTEN) AS BULLSEYE,
            pt.TOTAL AS SCORE,
            RANK() OVER (
                PARTITION BY ca.DESCRIPTION
                ORDER BY pt.TOTAL DESC, SUM(s.INNERTEN) DESC
            ) AS RANK_BY_CLASS,
            RANK() OVER (
                PARTITION BY co.TITLE
                ORDER BY pt.TOTAL DESC, SUM(s.INNERTEN) DESC
            ) AS RANK_BY_COMPETITION
        FROM
            PARTICIPANTS pa
            JOIN PERSONS p ON pa.PERSONID = p.PERSONID
            JOIN CLUBS c ON pa.CLUBID = c.CLUBID
            JOIN COMPETITIONS co ON pa.COMPETITIONID = co.COMPETITIONID
            JOIN SHOTS s ON pa.PARTICIPANTID = s.PARTICIPANTID
            JOIN PERSONALTOTALS pt ON pa.PARTICIPANTID = pt.PARTICIPANTID
            JOIN CLASSES cl ON pa.CLASSID = cl.CLASSID
            JOIN CATEGORIES ca ON cl.CATEGORYID = ca.CATEGORYID
        WHERE
            pa.COMPETITIONID = %s
        GROUP BY
            co.TITLE,
            ca.DESCRIPTION,
            p.FIRSTNAME,
            p.LASTNAME,
            c.CLUBNAME,
            pt.TOTAL,
            pa.PARTICIPANTID
        ORDER BY
            co.TITLE ASC,
            RANK_BY_COMPETITION ASC,
            ca.DESCRIPTION ASC,
            RANK_BY_CLASS ASC
        """
            % competition_id
        )

        connection = get_connection()
        cursor = connection.cursor()
        cursor.execute(query)
        columns = [desc[0] for desc in cursor.description]
        results = [dict(zip(columns, row)) for row in cursor.fetchall()]
        cursor.close()
        connection.close()

        return render_template("competition_results.html", results=results, view=view)

    return app
