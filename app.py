from flask import Flask, request, render_template_string, send_file
import zipfile
import os
from mashup import download_videos, trim_and_merge

app = Flask(__name__)

HTML_FORM = """
<h2>Mashup Web Application</h2>
<form method="post">
Singer Name: <input name="singer" required><br><br>
Number of Videos (>10): <input name="videos" required><br><br>
Duration in Seconds (>20): <input name="duration" required><br><br>
<button type="submit">Generate Mashup</button>
</form>
"""

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        singer = request.form["singer"]
        videos = int(request.form["videos"])
        duration = int(request.form["duration"])

        if videos <= 10:
            return "Number of videos must be greater than 10"

        if duration <= 20:
            return "Duration must be greater than 20 seconds"

        download_videos(singer, videos)
        trim_and_merge(duration, "mashup.mp3")

        with zipfile.ZipFile("mashup.zip", "w") as zipf:
            zipf.write("mashup.mp3")

        return send_file("mashup.zip", as_attachment=True)

    return render_template_string(HTML_FORM)


if __name__ == "__main__":
    app.run(debug=True)
