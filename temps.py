import pandas as pd

def calculate_time(population):
    if population < 250:
        return 30  # 30 minutes
    else:
        return 60  # 1 hour

# Read the Excel file
file_path = 'output.xlsx'  # Update with your file path
output_file_path = 'time_spent.txt'  # Output file path
df = pd.read_excel(file_path, engine='openpyxl')

# Create a list to store time spent in each place
time_spent_list = []

# Open the output file in write mode with proper encoding
with open(output_file_path, 'w', encoding='utf-8') as f:
    # Iterate over each row in the DataFrame
    for index, row in df.iterrows():
        time_spent = calculate_time(row['Population'])
        time_spent_list.append(time_spent)
        f.write(f"Temps d'espera a {row['Municipality']}: {time_spent} minuts\n")

    # Calculate the total time spent
    total_time = sum(time_spent_list)

    total_time_hours = total_time / 60
    # Write total time spent in hours

    f.write(f"\Temps d'espera totals : {total_time_hours:.2f} hours\n")

print("Time spent saved to time_spent.txt")
