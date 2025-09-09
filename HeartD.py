import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, classification_report

df = pd.read_csv("Datasets\sample_heart.csv") 


print("Sample Data:")
print(df.head())


X = df.drop('target', axis=1)
y = df['target']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

knn = KNeighborsClassifier(n_neighbors=3)
knn.fit(X_train, y_train)

y_pred = knn.predict(X_test)
print("\nModel Evaluation:")
print("Accuracy:", accuracy_score(y_test, y_pred))
print("\nClassification Report:\n", classification_report(y_test, y_pred))


print("\n--- Predict Heart Disease for New Patient ---")
try:
    user_data = [
        float(input("Age: ")),
        float(input("Gender (1=male, 0=female): ")),
        float(input("Chest Pain Type (0-3): ")),
        float(input("Resting Blood Pressure: ")),
        float(input("Cholesterol: ")),
        float(input("Fasting Blood Sugar > 120 mg/dl (1=True, 0=False): ")),
        float(input("Resting ECG (0-2): ")),
        float(input("Max Heart Rate Achieved: ")),
        float(input("Exercise Induced Angina (1=yes, 0=no): ")),
        float(input("ST Depression: ")),
        float(input("Slope of ST Segment (0-2): ")),
        float(input("Number of Major Vessels (0-3): ")),
        float(input("Thalassemia (1=normal, 2=fixed defect, 3=reversible defect): "))
    ]
   
    user_scaled = scaler.transform([user_data])
   
    user_pred = knn.predict(user_scaled)

    print("\nPrediction Result:", " Heart Disease Detected" if user_pred[0] == 1 else " No Heart Disease")

except Exception as e:
    print("Invalid input:", e)