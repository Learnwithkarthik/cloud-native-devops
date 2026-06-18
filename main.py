from flask import Flask

app = Flask(__name__)

# sample2
@app.route("/")
def home():
    return """
    <html>
        <body>
            <h1>Cloud Build Student Demo</h1>
            <p>This application image was created by Google Cloud Build.</p>
        </body>
    </html>
    """


@app.route("/health")
def health():
    return {
        "status": "healthy",
        "service": "student-app"
    }


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
