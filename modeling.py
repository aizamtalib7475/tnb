import pandas as pd
import pickle
from sklearn.linear_model import LinearRegression

data = pd.read_csv("electricity_usage.csv")
col = ['Fan', 'Refrigerator', 'AirConditioner', 'Television', 'MonthlyHours','ElectricityBill' ]
data = data[col]

target = "ElectricityBill"
X = data.drop(columns = [target])
y = data[target]

model = LinearRegression()
model.fit(X, y)

pickle.dump(model, open("LRmodel.pkl", "wb"))