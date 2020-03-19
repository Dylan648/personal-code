co2_data['Average'] = co2_data['Average'].replace(-99.99, math.nan)
co2_data.dropna(subset=['Average'], inplace=True)

