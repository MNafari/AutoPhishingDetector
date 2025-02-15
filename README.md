# AutoPhishingDetector

## 📌 Introduction
AutoPhishingDetector is an AI-powered phishing detection tool that analyzes messages and emails to determine the likelihood of phishing attempts.

## 🚀 Features
- Detects phishing attempts based on text analysis.
- Uses Machine Learning (Random Forest) and NLP (TF-IDF) techniques.
- Provides an API endpoint for checking messages.
- Trained with real phishing and non-phishing datasets.

## 🔧 Installation
### 1️⃣ Clone the repository:
```bash
git clone https://github.com/MNafari/AutoPhishingDetector.git
cd AutoPhishingDetector
```

### 2️⃣ Create and activate a virtual environment:
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
```

### 3️⃣ Install dependencies:
```bash
pip install -r requirements.txt
```

## 🏗️ Training the Model
To train the phishing detection model, run:
```bash
python src/model.py
```

## 🌍 Running the API
To start the Flask API, execute:
```bash
python src/app.py
```
The API will be available at `http://127.0.0.1:5000/`

## 📡 Using the API
To check if a message is phishing or not, send a POST request:
```bash
curl -X POST http://127.0.0.1:5000/detect -H "Content-Type: application/json" -d '{"message": "Your account has been compromised! Click here to secure it."}'
```
Response example:
```json
{
  "message": "Your account has been compromised! Click here to secure it.",
  "phishing_probability": 67.84
}
```

## 📝 License
This project is licensed under the MIT License.


