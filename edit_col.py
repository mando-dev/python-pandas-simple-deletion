import pandas as pd

# Load the data file into a DataFrame
df = pd.read_csv('converted2.csv')

# Drop a column by name
df = df.drop('congestion_surcharge', axis=1) # axis=1 for columns

#Get the number of rows in the DataFrame
num_rows = len(df)

# Calculate the index of the row to split the DataFrame
split_index = num_rows // 2

# Drop the rows after the split index
df = df.iloc[:split_index]


# Save the modified DataFrame to a new CSV file
df.to_csv('cong_surg_del.csv', index=False)
