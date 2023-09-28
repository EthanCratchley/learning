import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Read file path into dataframe
df = pd.read_csv('/Users/ethancratchley/desktop/appl_income_02.csv')

# Removing rows based on index
df.drop([5, 6, 15, 20, 24, 33, 34, 35, 37, 41, 42, 43, 44, 46], inplace=True)

# Removing Column
df.drop(df.columns[[6]], axis=1, inplace=True)

# Print head of dataframe
print(df.head(10))

# Save the cleaned Dataframe
df.to_csv('/Users/ethancratchley/desktop/appl_income_03.csv', index=False)
