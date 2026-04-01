import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("covid_data.csv")

print(data.head())

# Top 5 countries by cases
top = data.groupby("Country")["Confirmed"].sum().sort_values(ascending=False).head()

print(top)

top.plot(kind='bar')
plt.title("Top 5 Countries COVID Cases")
plt.show()
