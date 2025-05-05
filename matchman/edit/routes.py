import os

from flask import flash, redirect, render_template, request, url_for
from werkzeug.utils import secure_filename

from matchman.edit import edit

UPLOAD_FOLDER = "uploads"
ALLOWED_EXTENSIONS = {"fbk"}

# Ensure the upload folder exists
os.makedirs(UPLOAD_FOLDER, exist_ok=True)


def allowed_file(filename):
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS


@edit.route("/", methods=["GET", "POST"])
def upload_gbak():
    if request.method == "POST":
        # Check if the post request has the file part
        if "file" not in request.files:
            flash("No file part")
            return redirect(request.url)
        file = request.files["file"]
        # If the user does not select a file, browser may submit an empty part
        if file.filename == "":
            flash("No selected file")
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            filepath = os.path.join(UPLOAD_FOLDER, filename)
            file.save(filepath)
            return redirect(url_for("edit.upload_gbak"))
    return render_template("edit.html")
