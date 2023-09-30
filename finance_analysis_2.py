import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

def clean_data(file_path):
    """
    Clean the financial data by removing specific rows and columns.

    :param file_path: The file path of the CSV file to clean.
    :return: Cleaned DataFrame.
    """
    try:
        # Load the CSV data into a DataFrame
        df = pd.read_csv(file_path)

        # Define the indices of rows to drop
        rows_to_drop = [5, 6, 15, 20, 24, 33, 34, 35, 37, 41, 42, 43, 44, 46]

        # Drop the specified rows and a column
        df.drop(rows_to_drop, inplace=True)
        df.drop(df.columns[6], axis=1, inplace=True)

        # Print the cleaned DataFrame
        print(df.head(10))

        return df

    except FileNotFoundError:
        print(f"The file at path {file_path} does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Specify the file path
file_path = '/Users/ethancratchley/desktop/appl_income_02.csv'

# Call the clean_data function and get the cleaned DataFrame
cleaned_df = clean_data(file_path)

# Check if the DataFrame is not empty or None before saving it to a new CSV file
if cleaned_df is not None and not cleaned_df.empty:
    # Specify the path where the cleaned data will be saved
    cleaned_data_path = '/Users/ethancratchley/desktop/appl_income_03.csv'
    
    # Save the cleaned DataFrame to a new CSV file
    cleaned_df.to_csv(cleaned_data_path, index=False)
    print(f"Cleaned data saved to {cleaned_data_path}.")

