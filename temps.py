
import pandas as pd

def calculate_time(population, altitude):
    if population < 250:
        base_time = 30  # 30 minutes
    else:
        base_time = 60  # 1 hour
    
    if altitude > 800:
        altitude_difference = altitude - 800
        extra_time = altitude_difference * 0.005 * base_time  # 0.5% increment for each meter above 800m
        return base_time + extra_time
    else:
        return base_time

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
        time_spent = calculate_time(row['Population'], row['Altitude'])
        time_spent_list.append(time_spent)
        f.write(f"Temps d'espera a {row['Municipality']}: {time_spent} minuts\n")

    # Calculate the total time spent
    total_time = sum(time_spent_list)

    total_time_hours = total_time / 60
    # Write total time spent in hours

    f.write(f"\nTemps d'espera totals : {total_time_hours:.2f} hours\n")

print("Time spent saved to time_spent.txt")