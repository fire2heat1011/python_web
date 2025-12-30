from flask import Flask, render_template, request, jsonify
import joblib
import numpy as np

from routes import test_bp # routes 폴더에 있는 blueprint 파일을 가져온다.
from routes import view_bp
from routes import ai_bp
from routes import user_bp
from routes import board_bp

app = Flask(__name__)

app.register_blueprint(test_bp) # register_blueprint 함수를 사용하여 블루프린트를 등록할 수 있다.
app.register_blueprint(view_bp)
app.register_blueprint(ai_bp)
app.register_blueprint(user_bp)
app.register_blueprint(board_bp)

if __name__ == "__main__":
    app.run(debug=True, port=5000) # port 설정 가능