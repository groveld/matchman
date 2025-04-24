from firebird.driver import connect, driver_config
from flask import Flask, render_template

from config import Config


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    driver_config.read("firebird.cfg")

    @app.route("/", methods=["GET"])
    def index():
        return "Welcome to the Firebird API!"

    @app.route("/results", methods=["GET"])
    def get_results():
        query = """
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
            ) AS RANK
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
            pa.COMPETITIONID = 72
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
            ca.DESCRIPTION ASC,
            RANK ASC
        """
        connection = connect("matchmanager")
        cursor = connection.cursor()
        cursor.execute(query)
        columns = [desc[0] for desc in cursor.description]
        results = [dict(zip(columns, row)) for row in cursor.fetchall()]
        cursor.close()
        connection.close()

        # Group results by COMPETITION and CLASS
        grouped_results = {}
        for row in results:
            competition = row["COMPETITION"]
            class_name = row["CLASS"]
            if competition not in grouped_results:
                grouped_results[competition] = {}
            if class_name not in grouped_results[competition]:
                grouped_results[competition][class_name] = []
            grouped_results[competition][class_name].append(
                {
                    "FIRSTNAME": row["FIRSTNAME"],
                    "LASTNAME": row["LASTNAME"],
                    "CLUBNAME": row["CLUBNAME"],
                    "BULLSEYE": row["BULLSEYE"],
                    "SCORE": row["SCORE"],
                    "RANK": row["RANK"],
                }
            )

        # Convert grouped results to a list for rendering
        output = [
            {
                "COMPETITION": competition,
                "CLASSES": [
                    {"CLASS": class_name, "PARTICIPANTS": participants}
                    for class_name, participants in classes.items()
                ],
            }
            for competition, classes in grouped_results.items()
        ]
        return render_template("results.html", results=output)

    return app
