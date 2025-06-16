import pandas as pd
pd.options.display.max_rows = 9
pd.set_option("display.min_rows", 5) # This controls rows shown when truncated
print("max_rows value after the change : " + str(pd.options.display.max_rows))
print("min_rows value after the change : " + str(pd.options.display.min_rows))

df = pd.read_csv('cars_advanced.csv') # df has 15 rows
print(df)