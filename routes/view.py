from flask import Flask, render_template, Blueprint
import joblib

view_bp = Blueprint(
    "view",
    __name__,
    url_prefix="/"
)

# URL 주소로 함수 호출

@view_bp.route("/point1") # 127.0.0.1:5000/test1 로 주소 들어가면 됨
def home1():
    return render_template("frontend.html")

@view_bp.route("/point2") # 127.0.0.1:5000
def home2():
    return render_template("web.html")

@view_bp.route("/save_user") # 127.0.0.1:5000/save_user 에서 데이터를 받음
def save_user(): #2. 함수 이름
    return "Account saved!" #3. 함수 내용

if __name__ == "__main__":
    view_bp.run(debug=True)
