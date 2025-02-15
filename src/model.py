import joblib
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

# Sample training data
train_data = [
    "please verify your account",
    "click here to reset your password",
    "win a free gift now",
    "urgent! your account has been locked",
    "hello, how are you?",
    "meeting scheduled for tomorrow",
    "can you send the document?"
]
train_labels = [1, 1, 1, 1, 0, 0, 0]  # 1 = phishing, 0 = safe

# Train model
vectorizer = TfidfVectorizer()
X_train = vectorizer.fit_transform(train_data)
model = LogisticRegression()
model.fit(X_train, train_labels)

# Save model
joblib.dump(model, "models/updated_phishing_model.pkl")
joblib.dump(vectorizer, "models/updated_vectorizer.pkl")

print("Model trained and saved successfully!")
