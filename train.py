import pandas as pd
from sklearn.linear_model import LogisticRegression
import joblib

data = {
    "tenure": [1, 5, 2, 8, 10, 3, 7, 4],
    "monthly_charges": [100, 50, 80, 40, 30, 90, 45, 70],
    "churn": [1, 0, 1, 0, 0, 1, 0, 1]
}

df = pd.DataFrame(data)

X = df[["tenure", "monthly_charges"]]
y = df["churn"]

model = LogisticRegression()
model.fit(X, y)

joblib.dump(model, "churn_model.pkl")

print("Churn model trained successfully")
