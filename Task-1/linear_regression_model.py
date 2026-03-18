import pandas as pd
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score, mean_absolute_error

# Load dataset
data = pd.read_csv("train.csv")

# Select features
data = data[['GrLivArea', 'BedroomAbvGr', 'FullBath', 'OverallQual', 'SalePrice']]

# Drop missing values
data = data.dropna()

# Split data
X = data[['GrLivArea', 'BedroomAbvGr', 'FullBath', 'OverallQual']]
y = data['SalePrice']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
model = LinearRegression()
model.fit(X_train, y_train)

# Predict
y_pred = model.predict(X_test)

# Evaluation
mae = mean_absolute_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print("MAE:", mae)
print("MSE:", mse)
print("R2 Score:", r2)

# Visualization
plt.scatter(y_test, y_pred)
plt.xlabel("Actual Price")
plt.ylabel("Predicted Price")
plt.title("Actual vs Predicted Prices")
plt.savefig("result.png")   # saves graph
plt.show()

# Model info
print("Intercept:", model.intercept_)
print("Coefficients:", model.coef_)