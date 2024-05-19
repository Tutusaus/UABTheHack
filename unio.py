import pandas as pd

# Load the Excel files
file1 = pd.ExcelFile('montanya.xlsx')  # Workbook
file2 = pd.read_excel('municipis.xlsx')  # Single sheet file

# Extract population data from the second file
population_data = file2.iloc[:, 1]

# Initialize an empty DataFrame for the output
output_data = pd.DataFrame()

# Iterate through each sheet in file1 starting from the second sheet
for sheet_name in file1.sheet_names[1:]:
    # Extract altitude data from the current sheet
    altitude_data = file1.parse(sheet_name=sheet_name, usecols=[1], header=None).squeeze()
    
    # Check if municipalities match
    municipalities = file1.parse(sheet_name=sheet_name, usecols=[0], header=None).squeeze()

    # Create a DataFrame for the current sheet's output
    sheet_output = pd.DataFrame({'Municipality': municipalities})
    
    # Add altitude and population data
    sheet_output['Altitude'] = altitude_data
    sheet_output['Population'] = population_data
    
    # Concatenate current sheet's output with overall output
    output_data = pd.concat([output_data, sheet_output])

# Save the output to a new Excel file
output_data.to_excel('output.xlsx', index=False)
