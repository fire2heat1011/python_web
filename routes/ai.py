from flask import Blueprint, request, jsonify
import joblib
import numpy as np

ai_bp = Blueprint(
    "ai",
    __name__,
    url_prefix="/ai"
)

model = joblib.load("models/8_XGBClassifier_model.pkl")

label_map = {
    0: "setosa",
    1: "versicolor",
    2: "virginica"
}

# AI 예측 API
@ai_bp.route("/predicted_iris", methods=["POST"])
def predict_iris():
    data = request.get_json()

    if not data:
        return jsonify({"error": "JSON body required"}), 400

    try:
        sepal_length = float(data["sepal_length"])
        sepal_width = float(data["sepal_width"])
        petal_length = float(data["petal_length"])
        petal_width = float(data["petal_width"])
    except (KeyError, ValueError):
        return jsonify({"error": "Invalid input data"}), 400

    test_data = np.array([[
        sepal_length,
        sepal_width,
        petal_length,
        petal_width
    ]])

    prediction = model.predict(test_data)[0]

    return jsonify({
        "label_id": int(prediction),
        "label_name": label_map[prediction]
    }), 200
