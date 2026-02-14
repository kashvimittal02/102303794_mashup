from flask import Flask, request, render_template_string
from flask_mail import Mail, Message
from email_validator import validate_email, EmailNotValidError
import zipfile
import os
from mashup import download_videos, trim_and_merge

app = Flask(__name__)
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USERNAME'] = 'kashvi027@gmail.com'
app.config['MAIL_PASSWORD'] = 'ndgkpbnkpvvrvkgb'
app.config['MAIL_USE_TLS'] = True

mail = Mail(app)

HTML_FORM = """
<h2>Mashup Web Application</h2>
<form method="post">
Singer Name: <input name="singer" required><br><br>
Number of Videos (>10): <input name="videos" required><br><br>
Duration in Seconds (>20): <input name="duration" required><br><br>
Email ID: <input name="email" required><br><br>
<button type="submit">Generate Mashup</button>
</form>
"""

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        try:
            singer = request.form["singer"]
            videos = int(request.form["videos"])
            duration = int(request.form["duration"])
            email = request.form["email"]

            if videos <= 10:
                return "Number of videos must be greater than 10"

            if duration <= 20:
                return "Duration must be greater than 20 seconds"

            try:
                validate_email(email)
            except EmailNotValidError:
                return "Invalid email address"

            download_videos(singer, videos)
            trim_and_merge(duration, "mashup.mp3")

            with zipfile.ZipFile("mashup.zip", "w") as zipf:
                zipf.write("mashup.mp3")

            msg = Message(
                subject="Your Mashup File",
                sender=app.config['MAIL_USERNAME'],
                recipients=[email]
            )

            msg.body = "Your mashup file is attached."

            with open("mashup.zip", "rb") as f:
                msg.attach("mashup.zip", "application/zip", f.read())

            mail.send(msg)

            return "Mashup generated and sent to your email successfully!"

        except Exception as e:
            return f"Error occurred: {str(e)}"

    return render_template_string(HTML_FORM)


if __name__ == "__main__":
    app.run(debug=True)
