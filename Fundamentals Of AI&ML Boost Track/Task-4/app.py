from flask import Flask, request, jsonify
import joblib
import numpy as np

app = Flask(__name__)

model = joblib.load("Final_Exam_Score_Model.pkl")

@app.route("/")
def home():
    return "Prediction API"

@app.route("/predict", methods=["POST"])
def predict():
    data = request.json["features"]
    data = np.array(data).reshape(1, -1)
    result = model.predict(data)[0]
    return jsonify({"prediction": float(result)})

if __name__ == "__main__":
    app.run()
