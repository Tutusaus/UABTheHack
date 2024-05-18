import csv
import utm

def utm_to_lat_lon(utm_x, utm_y, zone_number, zone_letter):
    """
    Convert UTM coordinates to latitude and longitude.
    """
    lat, lon = utm.to_latlon(utm_x, utm_y, zone_number, zone_letter)
    return lat, lon

def convert_coordinates(input_file, output_file):
    """
    Read a CSV file and convert UTM coordinates to latitude and longitude,
    then write the results to a new CSV file.
    """
    with open(input_file, mode='r', newline='', encoding='utf-8') as infile, \
         open(output_file, mode='w', newline='', encoding='utf-8') as outfile:
        reader = csv.reader(infile)
        writer = csv.writer(outfile)

        # Write headers to output file
        headers = next(reader)
        writer.writerow(headers + ['Latitude', 'Longitude'])

        # Read each row and convert UTM coordinates
        for row in reader:
            if len(row) >= 2:
                utm_x = float(row[-2])  # Assuming UTMx is the second-to-last column
                utm_y = float(row[-1])  # Assuming UTMy is the last column
                zone_number = 32  # Example zone number (adjust as needed)
                zone_letter = 'N'  # Example zone letter (adjust as needed)

                # Convert UTM to lat/lon
                lat, lon = utm_to_lat_lon(utm_x, utm_y, zone_number, zone_letter)

                # Append lat/lon to the row and write to output file
                writer.writerow(row + [lat, lon])
            else:
                print(f"Skipping invalid row: {row}")

if __name__ == "__main__":
    input_file = 'csvloc.csv'
    output_file = 'output.csv'
    convert_coordinates(input_file, output_file)
