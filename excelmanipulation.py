import pandas as pd

def load_excel(file_path):
    # Load the Excel file into a pandas DataFrame with the specified engine
    df = pd.read_excel(file_path, engine='openpyxl')
    return df

def sort_dataframe(df, columns, ascending=True):
    # Sort the DataFrame by the specified columns
    sorted_df = df.sort_values(by=columns, ascending=ascending)
    return sorted_df

def save_excel(df, output_path):
    # Save the DataFrame to a new Excel file
    df.to_excel(output_path, index=False)

if __name__ == "__main__":
    # Specify the input and output file paths
    input_file = 'input.xlsx'
    output_file = 'sorted_output.xlsx'
    
    # Load the Excel file
    df = load_excel(input_file)
    
    # Specify the columns to sort by and the sort order
    columns_to_sort_by = ['Column1', 'Column2']  # Replace with actual column names
    sort_order = [True, False]  # True for ascending, False for descending for each column
    
    # Sort the DataFrame
    sorted_df = sort_dataframe(df, columns_to_sort_by, sort_order)
    
    # Save the sorted DataFrame to a new Excel file
    save_excel(sorted_df, output_file)
    
    print(f"Sorted data saved to {output_file}")
