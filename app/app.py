from flask import Flask, render_template, request
import joblib
import os

# Project root directory
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Create Flask app
app = Flask(
    __name__,
    template_folder="../templates",
    static_folder="static"
)

# Load trained model and scaler
model = joblib.load(os.path.join(BASE_DIR, "models", "fraud_model.pkl"))
scaler = joblib.load(os.path.join(BASE_DIR, "models", "scaler.pkl"))


# Home Page
import pandas as pd
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/dashboard")
def dashboard():

    df = pd.read_csv("../data/Transaction Fraud Detection for SafeBank.csv")

    total_transactions = len(df)

    fraud_transactions = df["IsFraud"].sum()

    genuine_transactions = total_transactions - fraud_transactions

    accuracy = {
        "KNN": 94.5,
        "Decision Tree": 86.5,
        "Random Forest": 94.5,
        "Naive Bayes": 94.5,
        "Ensemble": 94.5
    }

    return render_template(
        "dashboard.html",
        total=total_transactions,
        fraud=fraud_transactions,
        genuine=genuine_transactions,
        accuracy=accuracy
    )

# Run Flask App
if __name__ == "__main__":
    app.run(debug=True)