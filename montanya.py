import pandas as pd

def check_and_save_rows(file1, sheet_name_file1, file2, column_index_file1, column_index_file2, altitude_column_index_file2, output_file):
    # Read Excel files
    df1 = pd.read_excel(file1, sheet_name=sheet_name_file1)
    df2 = pd.read_excel(file2)

    # Check if content in specified columns match
    matching_rows = df1[df1.iloc[:, column_index_file1].isin(df2.iloc[:, column_index_file2])].copy()

    # Add altitude column to matching rows
    matching_rows['Altitude'] = df1.iloc[matching_rows.index, altitude_column_index_file2].values

    # Save matching rows to a text file
    matching_rows.to_csv(output_file, index=False)

if __name__ == "__main__":
    file1 = "Dades_Municipis.xlsx"
    sheet_name_file1 = "Ruta 2 "  # Specify the sheet name or index of file1
    file2 = "t15903.xlsx"
    column_index_file1 = 4  # Assuming the 5th column in file1
    column_index_file2 = 0  # Assuming the 1st column in file2
    altitude_column_index_file2 = 1  # Assuming the altitude column index in file2
    output_file = "matching_rows.txt"  # Name of the output text file

    check_and_save_rows(file1, sheet_name_file1, file2, column_index_file1, column_index_file2, altitude_column_index_file2, output_file)
