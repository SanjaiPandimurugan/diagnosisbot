import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import joblib

# Load the dataset
data = pd.read_csv('dataset.csv')  # Ensure this path is correct

# Print the first few rows of the DataFrame and the columns
print("DataFrame head:\n", data.head())
print("Columns in the dataset:", data.columns.tolist())  # Print as a list for clarity

# Ensure the expected columns are present
expected_columns = ['age', 'temperature', 'pulse', 'ecg', 'diagnosis']
missing_columns = [col for col in expected_columns if col not in data.columns]

if missing_columns:
    raise KeyError(f"Missing columns in the dataset: {missing_columns}")

# Prepare the features and target variable
X = data[['age', 'temperature', 'pulse', 'ecg']]
y = data['diagnosis']

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train the model
model = RandomForestClassifier()
model.fit(X_train, y_train)

# Save the trained model
joblib.dump(model, 'your_model.pkl')

print("Model trained and saved as 'your_model.pkl'")