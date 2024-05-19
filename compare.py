import pandas as pd

# Load the Excel files
file1 = 'Caps_de_municipi_de_Catalunya_georeferenciats.xlsx'
file2 = 'Dades_Municipis.xlsx'

# Specify the sheet in file1
sheet_name_1 = 'Worksheet'

# Read the Excel file1
df1 = pd.read_excel(file1, sheet_name=sheet_name_1)

# Specify the sheets in file2
sheets_file2 = ['Ruta 2 ', 'Ruta 4 ', 'Ruta 5 ']  # Update with actual sheet names

# Specify the column to compare from file1
column_to_compare_1 = df1.columns[0]  # First column in file1

# Create a list to hold the merged DataFrames
merged_dfs = []

# Iterate over each sheet in file2
for sheet_name_2 in sheets_file2:
    # Read the Excel file2
    df2 = pd.read_excel(file2, sheet_name=sheet_name_2)

    # Specify the column to compare from file2
    column_to_compare_2 = df2.columns[4]  # 5th column in file2 (index 4)

    # Merge DataFrames based on the specified columns to find matches
    merged_df = pd.merge(df1, df2, left_on=column_to_compare_1, right_on=column_to_compare_2)

    # Add the merged DataFrame to the list
    merged_dfs.append(merged_df)

# Concatenate all merged DataFrames into a single DataFrame
final_merged_df = pd.concat(merged_dfs, ignore_index=True)

# Save the final merged DataFrame to a new Excel file
final_merged_df.to_excel('merged_result_all_sheets.xlsx', index=False)

print("All merged DataFrames have been concatenated and saved to 'merged_result_all_sheets.xlsx'")
