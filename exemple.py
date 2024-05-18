import googlemaps

# Replace with your Google Maps API key
API_KEY = 'AIzaSyDm2j6XB4FX6e8rZ5F0GsjVv_2CNvQqz_8'
gmaps = googlemaps.Client(key=API_KEY)

def read_locations_from_file(file_path):
    """
    Reads locations from a text file.
    """
    with open(file_path, 'r') as file:
        locations = [line.strip() for line in file]
    return locations

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

def write_sorted_locations_to_file(sorted_locations, output_file):
    """
    Writes sorted locations to a text file.
    """
    with open(output_file, 'w') as file:
        for location in sorted_locations:
            file.write(location + '\n')

if __name__ == "__main__":
    # 1. Read locations from file
    locations = read_locations_from_file('locations.txt')

    # 2. Get the optimized route
    route = get_optimized_route(locations)

    # 4. Extract sorted locations from the route
    sorted_locations = [leg['start_address'] for leg in route]
    sorted_locations.append(route[-1]['end_address'])

    # 5. Write sorted locations to file
    write_sorted_locations_to_file(sorted_locations, 'sorted_locations.txt')
