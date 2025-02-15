import xgboost as xgb
import joblib
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import pandas as pd


df = pd.read_csv("data/expanded_phishing_dataset.csv")


X = df["message"]
y = df["label"]


vectorizer = TfidfVectorizer()
X_tfidf = vectorizer.fit_transform(X)


X_train, X_test, y_train, y_test = train_test_split(X_tfidf, y, test_size=0.2, random_state=42)


xgb_model = xgb.XGBClassifier(n_estimators=150, learning_rate=0.05,max_depth=5, use_label_encoder=False, eval_metric='logloss')


xgb_model.fit(X_train, y_train)


y_pred = xgb_model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)


joblib.dump(xgb_model, "models/xgb_phishing_model.pkl")
joblib.dump(vectorizer, "models/xgb_vectorizer.pkl")


print(f"XGBoost Accuracy: {accuracy * 100:.2f}%")

