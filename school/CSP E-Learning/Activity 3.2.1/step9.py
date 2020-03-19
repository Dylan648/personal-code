# TODO #2: Use matplotlib to make a line graph
plt.plot(temp_data['Year'], temp_data['Anomaly'], color='gray')
plt.ylabel('Temperature Anomalies in Celsius')
plt.xlabel('Years')
plt.title('Change in Temperatures')

