import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error

# Load cleaned data
file_path = "data/processed/cleaned_sales_data.csv"

try:
    df = pd.read_csv(file_path)
    print("Cleaned data loaded.")
except FileNotFoundError:
    print("Run data_cleaning.py first.")
    exit()

# Check columns
print("Columns:", df.columns)

# Assume dataset has 'Sales' column
if "Sales" not in df.columns:
    print("Dataset must contain a 'Sales' column.")
    exit()

# Create simple feature using index
df["Index"] = range(len(df))

X = df[["Index"]]
y = df["Sales"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

model = LinearRegression()
model.fit(X_train, y_train)

predictions = model.predict(X_test)

mae = mean_absolute_error(y_test, predictions)

print("Model trained successfully.")
print("Mean Absolute Error:", mae)


import matplotlib.pyplot as plt

plt.scatter(X_test, y_test)
plt.plot(X_test, predictions)
plt.xlabel("Time Index")
plt.ylabel("Sales")
plt.title("Actual vs Predicted Sales")
plt.show()
