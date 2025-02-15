import joblib
from flask import Flask, request, jsonify
from preprocess import clean_text

# Load updated model
model = joblib.load("models/updated_phishing_model.pkl")
vectorizer = joblib.load("models/updated_vectorizer.pkl")

app = Flask(__name__)

@app.route("/detect", methods=["POST"])
def detect_phishing():
    data = request.json
    text = data.get("message", "")
    clean_msg = clean_text(text)
    text_vectorized = vectorizer.transform([clean_msg])
    prediction = model.predict_proba(text_vectorized)[0][1]  # Probability of phishing

    response = {
        "message": text,
        "phishing_probability": round(prediction * 100, 2)
    }
    return jsonify(response)

@app.route("/")
def home():
    return jsonify({"message": "AutoPhishingDetector API is running with updated model!"})

if __name__ == "__main__":
    app.run(debug=True)

