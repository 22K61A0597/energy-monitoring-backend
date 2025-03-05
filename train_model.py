import numpy as np
from sklearn.linear_model import LinearRegression
import pickle
import os

# Sample training data (Replace with real data if available)
X_train = np.array([[22, 55, 15], [30, 60, 12], [18, 50, 20]])
y_train = np.array([100, 150, 80])  # Example energy consumption

# Train the model
model = LinearRegression()
model.fit(X_train, y_train)

# Ensure models directory exists
os.makedirs("models", exist_ok=True)

# Save the trained model
with open("models/energy_model.pkl", "wb") as f:
    pickle.dump(model, f)

print("✅ Model trained and saved successfully!")
