from flask import Flask, redirect, url_for, session, request, render_template
from authlib.integrations.flask_client import OAuth
from dotenv import load_dotenv
import os
from datetime import datetime

load_dotenv()

app = Flask(__name__)
app.secret_key = "development"

oauth = OAuth(app)

oauth.register(
    name="suap",
    client_id=os.getenv("CLIENT_ID"),
    client_secret=os.getenv("CLIENT_SECRET"),
    api_base_url="https://suap.ifrn.edu.br/api/",
    request_token_url=None,
    access_token_method="POST",
    access_token_url="https://suap.ifrn.edu.br/o/token/",
    authorize_url="https://suap.ifrn.edu.br/o/authorize/",
    fetch_token=lambda: session.get("suap_token")
)


def usuario():
    return oauth.suap.get("rh/meus-dados").json()


@app.route("/")
def index():
    if "suap_token" not in session:
        return render_template("index.html")

    return redirect(url_for("user"))


@app.route("/user")
def user():

    if "suap_token" not in session:
        return redirect(url_for("index"))

    return render_template(
        "user.html",
        user_data=usuario()
    )
    
    
@app.route("/boletim")
def boletim():

    if "suap_token" not in session:
        return redirect(url_for("index"))

    ano = request.args.get("ano", "2026")

    response = oauth.suap.get(f"ensino/meu-boletim/{ano}/1")

    boletim = response.json()["results"]

    return render_template(
        "boletim.html",
        user_data=usuario(),
        boletim=boletim,
        ano=ano)
    
    
@app.route("/login")
def login():
    redirect_uri = url_for("auth", _external=True)
    return oauth.suap.authorize_redirect(redirect_uri)


@app.route("/login/authorized")
def auth():
    token = oauth.suap.authorize_access_token()
    session["suap_token"] = token
    return redirect(url_for("user"))


@app.route("/logout")
def logout():
    session.pop("suap_token", None)
    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(debug=True)