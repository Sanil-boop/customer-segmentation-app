from flask import Flask, render_template, request
import joblib
import numpy as np

app = Flask(__name__)

model = joblib.load("customer_model.pkl")
scaler = joblib.load("scaler.pkl")

cluster_labels = {
    0: "Premium High Spender 💎",
    1: "Budget Saver 🧾",
    2: "Careful Wealthy Spender 🧐",
    3: "Young Impulsive Buyer ⚡",
    4: "Average Customer 🙂"
}

@app.route("/", methods=["GET","POST"])
def index():
    segment = None

    if request.method == "POST":
        income = float(request.form["income"])
        score = float(request.form["score"])

        data = scaler.transform([[income, score]])
        cluster = model.predict(data)[0]

        segment = cluster_labels[cluster]

    return render_template("index.html", segment=segment)

if __name__ == "__main__":
    app.run()
