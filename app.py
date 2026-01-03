from flask import Flask, render_template, request
import joblib
import numpy as np

app = Flask(__name__)

model = joblib.load("customer_model.pkl")
scaler = joblib.load("scaler.pkl")

cluster_labels = {
    1: "Premium High Spender 💎",
    4: "Budget Saver 🧾",
    3: "Careful Wealthy Spender 🧐",
    2: "Young Impulsive Buyer ⚡",
    0: "Average Customer 🙂"
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
