import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix

import joblib


# ==========================================
# LOAD DATASET
# ==========================================

DATASET = "../data/gestures.csv"

df = pd.read_csv(DATASET)

print("Dataset loaded")
print("Shape:", df.shape)


# ==========================================
# FEATURES AND LABEL
# ==========================================

FEATURES = [
    "THUMB",
    "INDEX",
    "MIDDLE",
    "RING",
    "LITTLE",
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
# TRAIN / TEST SPLIT
# ==========================================

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42,
    stratify=y
)

print()
print("Training samples:", len(X_train))
print("Testing samples:", len(X_test))


# ==========================================
# RANDOM FOREST MODEL
# ==========================================

model = RandomForestClassifier(
    n_estimators=200,
    random_state=42,
    class_weight="balanced"
)


# ==========================================
# TRAIN
# ==========================================

print()
print("Training Random Forest...")

model.fit(X_train, y_train)

print("Training complete!")


# ==========================================
# PREDICTION
# ==========================================

y_pred = model.predict(X_test)


# ==========================================
# ACCURACY
# ==========================================

accuracy = accuracy_score(
    y_test,
    y_pred
)

print()
print("================================")
print("          RESULTS")
print("================================")

print()
print(
    f"Accuracy: {accuracy * 100:.2f}%"
)


# ==========================================
# CLASSIFICATION REPORT
# ==========================================

print()
print("Classification Report:")
print()

print(
    classification_report(
        y_test,
        y_pred
    )
)


# ==========================================
# CONFUSION MATRIX
# ==========================================

print()
print("Confusion Matrix:")
print()

print(
    confusion_matrix(
        y_test,
        y_pred
    )
)


# ==========================================
# FEATURE IMPORTANCE
# ==========================================

print()
print("Feature Importance:")
print()

importance = pd.Series(
    model.feature_importances_,
    index=FEATURES
).sort_values(
    ascending=False
)

print(importance)


# ==========================================
# SAVE MODEL
# ==========================================

MODEL_FILE = "gesture_model.pkl"

joblib.dump(
    model,
    MODEL_FILE
)

print()
print("================================")
print("MODEL SAVED")
print("================================")

print()
print("Saved as:", MODEL_FILE)
