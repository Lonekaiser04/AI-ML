import tkinter as tk
from tkinter import messagebox
import numpy as np
import joblib

# Load trained model
model = joblib.load("decisiontree_model.pkl")

def predict():
    try:
        # Get input values
        data = [float(entry.get()) for entry in entries]
        data_array = np.array(data).reshape(1, -1)
        
        # Predict
        prediction = model.predict(data_array)[0]
        result = "Diabetes Detected" if prediction == 1 else "No Diabetes Detected"
        messagebox.showinfo("Prediction Result", result)
        
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numbers in all fields")
    except Exception as e:
        messagebox.showerror("Error", f"An unexpected error occurred: {str(e)}")

# Create main window
root = tk.Tk()
root.title("Diabetes Prediction using Decision Tree")
root.resizable(False, False)

# Input fields configuration
labels = [
    "Pregnancies", "Glucose", "BloodPressure", "SkinThickness",
    "Insulin", "BMI", "DiabetesPedigreeFunction", "Age"
]

entries = []
for i, label in enumerate(labels):
    frame = tk.Frame(root)
    frame.grid(row=i, column=0, sticky="ew", padx=10, pady=5)
    
    tk.Label(frame, text=label + ":", width=25, anchor="w").pack(side="left")
    entry = tk.Entry(frame, width=15)
    entry.pack(side="right", padx=(10, 0))
    entries.append(entry)

# Prediction button
predict_btn = tk.Button(
    root, 
    text="Predict Diabetes", 
    command=predict,
    bg="#3BC240",
    fg="white",
    padx=10,
    pady=5
)
predict_btn.grid(row=len(labels), column=0, pady=15)

# Run the application

root.mainloop()
