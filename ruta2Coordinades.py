import pandas as pd

# Load the Excel file
file_path = "merged_result_all_sheets.xlsx"
df = pd.read_excel(file_path)

# Swap columns Longitud and Latitud
df['Longitud'], df['Latitud'] = df['Latitud'], df['Longitud']

# Extract Longitud and Latitud columns
longitud_latitud = df[['Longitud', 'Latitud']]

# Convert to string and concatenate Longitud and Latitud with a space separator
longitud_latitud_str = longitud_latitud.astype(str).apply(lambda x: ' '.join(x), axis=1)

# Save to a text file without quotation marks and commas
output_file = "locations.txt"
with open(output_file, 'w') as f:
    for line in longitud_latitud_str:
        f.write(line + '\n')

print("Data saved to", output_file)
