import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# Load dataset
data = pd.read_csv("data/energy_data.csv")

# Prepare features and labels
X = data[['temperature', 'humidity']]
y = data['energy_consumption']

# Split the data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train the model
model = LinearRegression()
model.fit(X_train, y_train)

# Save the trained model
joblib.dump(model, "models/energy_model.pkl")

print("Model training complete. Saved as 'energy_model.pkl'.")
