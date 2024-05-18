import googlemaps
import pandas as pd

# Replace with your Google Maps API key
API_KEY = 'AIzaSyDm2j6XB4FX6e8rZ5F0GsjVv_2CNvQqz_8'
gmaps = googlemaps.Client(key=API_KEY)

def read_locations_from_file(file_path):
    """
    Reads locations from a file (e.g., CSV, TXT)
    """
    # Adjust this based on your file format 
    df = pd.read_excel(file_path)
    return df['Address'].tolist()

def get_optimized_route(locations):
    """
    Uses the Google Maps Directions API to get the shortest route.
    """
    # Create a request for the Google Maps Directions API
    directions_result = gmaps.directions(
        origin=locations[0],  
        destination=locations[-1], 
        waypoints=locations[1:-1],
        optimize_waypoints=True  # Key for route optimization
    )

    # Extract the optimized route information
    route = directions_result[0]['legs']
    return route

def print_route_details(route):
    """
    Prints the steps and total distance of the optimized route.
    """
    total_distance = 0
    for leg in route:
        print(f"From: {leg['start_address']}")
        for step in leg['steps']:
            print(f"- {step['html_instructions']}") 
        print(f"To: {leg['end_address']}")
        total_distance += leg['distance']['value']
    print(f"\nTotal Distance: {total_distance / 1000:.2f} km")

if __name__ == "__main__":
    # 1. Read locations from file
    locations = read_locations_from_file('Dades_Municipis.xlsx')

    # 2. Get the optimized route
    route = get_optimized_route(locations)

    # 3. Print route details
    print_route_details(route) 
