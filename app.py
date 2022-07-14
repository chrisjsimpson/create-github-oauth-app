from flask import Flask, render_template
import os
from dotenv import load_dotenv

load_dotenv(verbose=True)

GITHUB_OAUTH_CLIENT_ID = os.getenv("GITHUB_OAUTH_CLIENT_ID")

app = Flask(__name__)


@app.route("/")
def index():
    client_id = GITHUB_OAUTH_CLIENT_ID
    github_authorize_url = (
        f"https://github.com/login/oauth/authorize?client_id={client_id}"  # noqa: E501
    )
    return render_template(
        "index.html", github_authorize_url=github_authorize_url
    )  # noqa: E501
