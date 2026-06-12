import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix


# 1. Load data
df = pd.read_csv("survey lung cancer.csv")

print("First rows:")
print(df.head())

print("\nColumns:")
print(df.columns)

# 2. Clean column names
df.columns = df.columns.str.strip()

# 3. Convert text columns to numbers
df["GENDER"] = df["GENDER"].map({"M": 0, "F": 1})
df["LUNG_CANCER"] = df["LUNG_CANCER"].map({"NO": 0, "YES": 1})

# 4. Define input data X and target y
X = df.drop("LUNG_CANCER", axis=1)
y = df["LUNG_CANCER"]

# 5. Split data into train and test
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

# 6. Train model
model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)

# 7. Predict
y_pred = model.predict(X_test)

# 8. Evaluate
accuracy = accuracy_score(y_test, y_pred)

print("\nAccuracy:")
print(accuracy)

print("\nConfusion matrix:")
print(confusion_matrix(y_test, y_pred))

print("\nClassification report:")
print(classification_report(y_test, y_pred))

# 9. Show feature importance
importance = pd.DataFrame({
    "Feature": X.columns,
    "Coefficient": model.coef_[0]
})

importance["Abs_Coefficient"] = importance["Coefficient"].abs()
importance = importance.sort_values("Abs_Coefficient", ascending=False)

print("\nMost important features:")
print(importance[["Feature", "Coefficient"]])