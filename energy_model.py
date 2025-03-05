import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import joblib

# Step 1: Generate or Load Energy Data
def generate_data():
    np.random.seed(42)
    days = np.arange(1, 101)  # 100 days of data
    energy_usage = 100 + 2 * days + np.random.normal(0, 10, 100)  # Simple pattern with noise

    data = pd.DataFrame({'Day': days, 'EnergyUsage': energy_usage})
    return data

# Step 2: Train the AI Model
def train_model():
    data = generate_data()
    X = data[['Day']]
    y = data['EnergyUsage']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    model = LinearRegression()
    model.fit(X_train, y_train)

    # Save the trained model
    joblib.dump(model, 'energy_model.pkl')

    print("Model trained and saved successfully!")

if __name__ == "__main__":
    train_model()
