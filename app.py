# EJERCICIO 06.3 - Group By
import pandas as pd
data_frame = pd.read_csv(".learn/assets/us_baby_names_right.csv")
print(data_frame.head(5))

# Value Counts
result = data_frame.groupby(by=["Name"]).sum()
print(len(result))