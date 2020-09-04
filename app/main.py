from flask import render_template, jsonify, request, redirect
from flask_cors import CORS, cross_origin
from app import app, login
from app.models.models import *
from flask_login import login_user
import hashlib

cors = CORS(app, resources={r"/*": {"origins": "*"}})


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/test", methods=['post'])
def test():
    return jsonify({'test': 1})


@login.user_loader
def user_load(user_id):
    return User.query.get(user_id)


@app.route("/login-admin", methods=['GET', 'POST'])
def login_admin():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password", "")
        user = User.query.filter(User.username == username.strip(),
                                 User.password == password.strip()).first()
        if user:
            login_user(user=user)

    return redirect("/admin")


if __name__ == "__main__":
    app.run(debug=True)  # MỞ chế độ debug cho development
