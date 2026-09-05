# AdaptiveSign
# Random Forest Gesture Classification

import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix


# ==========================================
# 1. Load Dataset
# ==========================================

DATASET_PATH = "../data/gestures.csv"

df = pd.read_csv(DATASET_PATH)

print("Dataset loaded successfully!")
print("Dataset shape:", df.shape)

print("\nFirst 5 samples:")
print(df.head())


# ==========================================
# 2. Define Features and Labels
# ==========================================

FEATURES = [
    "F1",
    "F2",
    "F3",
    "F4",
    "F5",
    "AX",
    "AY",
    "AZ",
    "GX",
    "GY",
    "GZ"
]

X = df[FEATURES]
y = df["LABEL"]


# ==========================================
# 3. Split Dataset
# ==========================================

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

print("\nTraining samples:", len(X_train))
print("Testing samples:", len(X_test))


# ==========================================
# 4. Create Random Forest Model
# ==========================================

model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)


# ==========================================
# 5. Train Model
# ==========================================

print("\nTraining model...")

model.fit(X_train, y_train)

print("Training completed!")


# ==========================================
# 6. Prediction
# ==========================================

y_pred = model.predict(X_test)


# ==========================================
# 7. Accuracy
# ==========================================

accuracy = accuracy_score(y_test, y_pred)

print("\n==============================")
print("MODEL PERFORMANCE")
print("==============================")

print(f"Accuracy: {accuracy * 100:.2f}%")


# ==========================================
# 8. Classification Report
# ==========================================

print("\nClassification Report:")
print(classification_report(y_test, y_pred))


# ==========================================
# 9. Confusion Matrix
# ==========================================

print("\nConfusion Matrix:")
print(confusion_matrix(y_test, y_pred))
