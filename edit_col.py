#deleting a single column in your DB

import pandas as pd

df = pd.read_csv('fileName.csv')

df = df.drop('column_name', axis=1) # axis=1 for columns

df.to_csv('converted2.csv', index=False)

