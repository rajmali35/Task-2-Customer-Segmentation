Task-01: House Price Prediction using Linear Regression

Objective:
To develop a machine learning model that predicts house prices based on key features such as living area, number of bedrooms, bathrooms, and overall quality of the house.

Tools & Technologies Used:

* Python
* Pandas
* NumPy
* Scikit-learn
* Matplotlib

Dataset:
The dataset used is the House Prices dataset from Kaggle, which contains various features related to residential homes.

Process:

1. Loaded the dataset using Pandas
2. Selected important features: GrLivArea, BedroomAbvGr, FullBath, OverallQual
3. Handled missing values by removing null entries
4. Split the dataset into training and testing sets (80:20 ratio)
5. Applied Linear Regression model using Scikit-learn
6. Predicted house prices on test data
7. Evaluated model performance using:

   * Mean Absolute Error (MAE): 28290.36
   * Mean Squared Error (MSE): 1832990106.76
   * R2 Score: 0.7610
8. Visualized results using a scatter plot (Actual vs Predicted Prices)

Results:
The model achieved an R2 score of 0.7610, indicating a good relationship between selected features and house prices.

Conclusion:
The Linear Regression model was able to predict house prices with good accuracy. The visualization shows that predicted values are reasonably close to actual values, demonstrating effective model performance. The model can be further improved by including more relevant features and applying advanced machine learning algorithms.
