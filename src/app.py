import joblib
import tldextract
import re
from flask import Flask, request, jsonify
from preprocess import clean_text, extract_links

# Load trained model and vectorizer
model = joblib.load("models/updated_phishing_model.pkl")
vectorizer = joblib.load("models/updated_vectorizer.pkl")

app = Flask(__name__)

@app.route("/detect", methods=["POST"])
def detect_phishing():
    """
    API endpoint to detect phishing probability of a given message.
    It also checks if the message contains suspicious links.
    """
    data = request.json
    text = data.get("message", "")

    # Clean the input text
    clean_msg = clean_text(text)
    text_vectorized = vectorizer.transform([clean_msg])
    prediction = model.predict_proba(text_vectorized)[0][1]  # Get phishing probability

    is_phishing = bool(prediction > 0.6)  # Convert to boolean
    phishing_prob = float(round(prediction * 100, 2))  # Convert probability to float

    # Extract suspicious links from the text
    links = extract_links(text)
    has_suspicious_links = len(links) > 0  # True if links are present

    response = {
        "message": text,
        "phishing_probability": phishing_prob,
        "is_phishing": is_phishing,
        "contains_suspicious_links": has_suspicious_links,
        "extracted_links": links  # List of extracted domain names
    }

    return jsonify(response)

@app.route("/")
def home():
    """
    Home endpoint to check if the API is running.
    """
    return jsonify({"message": "AutoPhishingDetector API is running with updated model!"})

if __name__ == "__main__":
    app.run(debug=True)

