# 🚀 AutoPhishingDetector - AI-Based Phishing Detection API

AutoPhishingDetector is a machine learning-based API that detects phishing messages and identifies suspicious links.

## 🔥 Features
- Detects phishing messages with **XGBoost** model.
- Analyzes messages for **suspicious links**.
- Provides **REST API** for easy integration.

## 🛠 Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/MNafari/AutoPhishingDetector.git
   cd AutoPhishingDetector
   ```

2. **Create a virtual environment** and activate it:
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On macOS/Linux
   venv\Scripts\activate     # On Windows
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

## 🚀 How to Run
1. **Start the API server**:
   ```bash
   python src/app.py
   ```

2. **Test API with curl**:
   ```bash
   curl -X POST http://127.0.0.1:5000/detect -H "Content-Type: application/json" -d '{"message": "Congratulations! You have won a $500 Amazon gift card. Click here to claim it now."}'
   ```

3. **Expected response**:
   ```json
   {
     "message": "Congratulations! You have won a $500 Amazon gift card. Click here to claim it now.",
     "phishing_probability": 61.67,
     "is_phishing": true,
     "contains_suspicious_links": false,
     "extracted_links": []
   }
   ```

## 📦 Deploy with Docker (Optional)
1. **Build Docker image**:
   ```bash
   docker build -t phishing-detector .
   ```

2. **Run the container**:
   ```bash
   docker run -p 5000:5000 phishing-detector
   ```

## 📜 License
This project is licensed under the **MIT License**.


