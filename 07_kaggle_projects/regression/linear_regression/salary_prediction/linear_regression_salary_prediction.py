# LOAD DATA
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('datasets/Salary_dataset.csv')
df.head()

df.info()

df = df.loc[:, ['YearsExperience', 'Salary']]
df

# DATA PROCESSING
x = df["YearsExperience"].values
y = df["Salary"].values

n = len(x)

# MODELING
sum_x = np.sum(x)
sum_y = np.sum(y)
sum_xy = np.sum(x*y)
sum_x2 = np.sum(x*x)

a = (sum_y * sum_x2 - sum_x * sum_xy) / (n * sum_x2 - sum_x**2)
b = (n * sum_xy - sum_x * sum_y) / (n * sum_x2 - sum_x**2)

yearsExp = 2.1
salary_pred = a + b * yearsExp
print("Years Experience:", yearsExp, "| Salary Prediction: ", salary_pred)

# EVALUATION
y_pred = a + b * x

SS_res = np.sum((y - y_pred)**2)
SS_tot = np.sum((y - np.mean(y))**2)
r2 = 1 - SS_res/SS_tot

mae = np.mean(np.abs(y - y_pred))
mse = np.mean((y - y_pred)**2)
rmse = np.sqrt(mse)

print("Model Performance:")
print("MAE: ", mae)
print("MSE: ", mse)
print("RMSE:", rmse)
print("R-squared:", r2)

# VISUALIZATION
plt.title("Linear Regression: Salary vs Years of Experience")
plt.scatter(x, y, color="blue", label="Data asli")
plt.plot(x, y_pred, color="red", label="Regresi linear")
plt.xlabel("Years Experience")
plt.ylabel("Salary")
plt.legend()
plt.show()

