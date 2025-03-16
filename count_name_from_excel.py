import pandas as pd

def count_names_from_csv(file_path, column_name):
    """
    Counts the occurrences of each unique name in a specified column of an Excel file.

    Args:
        file_path (str): The path to the Excel file.
        column_name (str): The name of the column containing the names.

    Returns:
        pandas.Series: A pandas Series with names as index and counts as values, or None if an error occurs.
    """
    try:
        df = pd.read_csv(file_path)
        if column_name not in df.columns:
            print(f"Error: Column '{column_name}' not found in the Excel file.")
            return None

        name_counts = df[column_name].value_counts()
        return name_counts

    except FileNotFoundError:
        print(f"Error: File not found at '{file_path}'.")
        return None
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None

# Example usage:
file_path = "D:/python_test.csv"  # Replace with your Excel file path
column_name = "Names"  # Replace with the name of the column containing names

name_counts = count_names_from_csv(file_path, column_name)

if name_counts is not None:
    print(name_counts)