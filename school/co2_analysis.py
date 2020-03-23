import matplotlib.pyplot as plt
import pandas as pd
import math

co2_data = pd.read_csv("co2_data.csv", header=0)
print(co2_data)
co2_data['Average'] = co2_data['Average'].replace(-99.99, math.nan)
print(co2_data)
co2_data.dropna(subset=['Average'], inplace=True)
print(co2_data)


# plt.plot(co2_data['Year'], co2_data['Average'], color='blue')
# plt.ylabel('CO2 Levels in ppm')
# plt.xlabel('Years')
# plt.title('Change in Carbon Dioxide Levels')

plt.show()