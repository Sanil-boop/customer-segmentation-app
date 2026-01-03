# 🛍️ Customer Segmentation Using K-Means (Machine Learning + Flask Web App)

This project applies **K-Means Clustering** to group retail store customers based on their:

- Annual Income
- Spending Score

The goal is to help businesses identify **customer behavior patterns** and create targeted marketing strategies.

The model is integrated into a **Flask web application** where users can input customer details and receive a predicted segment.

---

## 🌐 Live Demo

🚀 Web App: https://customer-segmentation-app-x6xn.onrender.com

> Hosted on Render (Free Tier)

---

## 📊 Project Objective

Customer segmentation helps businesses:

✔ Identify premium / high-value customers  
✔ Recognize budget-conscious shoppers  
✔ Detect impulsive buyers  
✔ Improve marketing ROI  
✔ Personalize offers & recommendations  

This project demonstrates how Machine Learning can support **business decision making**.

---

## 🧠 Machine Learning Model

### Algorithm Used

- **K-Means Clustering**

### Features Used

| Feature | Description |
|--------|----------|
| Annual Income (k$) | Customer yearly income |
| Spending Score (1–100) | Customer purchasing behavior score |

### Output Clusters (Example Interpretation)

| Cluster | Type |
|--------|------|
| 💎 Premium High Spenders |
| 🧾 Budget Conscious Customers |
| ⚡ Impulsive Buyers |
| 🙂 Average Spenders |
| 🧐 Wealthy but Cautious Spenders |

---

## 🗂 Dataset

Dataset Source (Kaggle):

Customer Segmentation / Mall Customers Dataset

https://www.kaggle.com/datasets/vjchoudhary7/customer-segmentation-tutorial-in-python

Dataset Columns:

- Customer ID
- Gender
- Age
- Annual Income
- Spending Score

---

## 🏗️ Tech Stack

**Programming Language**
- Python

**Machine Learning**
- Scikit-Learn
- K-Means Clustering
- StandardScaler

**Backend**
- Flask

**Frontend**
- HTML
- CSS

**Deployment**
- Render (Cloud Hosting)

---

## 🧩 Project Workflow

1️⃣ Load and explore dataset  
2️⃣ Select features (Income & Spending Score)  
3️⃣ Scale data using StandardScaler  
4️⃣ Apply K-Means clustering  
5️⃣ Determine optimal K using Elbow Method  
6️⃣ Save trained model using Joblib  
7️⃣ Integrate with Flask web app  
8️⃣ Deploy to Render

---

## 🖥️ Web App Features

✔ User enters Income & Spending Score  
✔ Model predicts customer segment  
✔ Displays segment meaning  
✔ Clean & aesthetic UI  
✔ Works online in browser

---

## 🚀 Run Locally (Development Mode)

### Clone the repository

```bash
git clone https://github.com/your-username/customer-segmentation-flask.git
cd customer-segmentation-flask
