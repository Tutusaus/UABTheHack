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
    total_waypoints = len(locations) - 2  # Excluding the start and end locations
    max_waypoints_per_request = 25
    num_requests = (total_waypoints + max_waypoints_per_request - 1) // max_waypoints_per_request

    # Initialize the route
    route = []

    # Make multiple requests to handle all waypoints
    for i in range(num_requests):
        start_index = i * (max_waypoints_per_request - 2)
        end_index = min(start_index + max_waypoints_per_request - 1, total_waypoints)  # Exclude start and end
        waypoints_chunk = locations[start_index:end_index]
        
        # Create a request for the Google Maps Directions API
        directions_result = gmaps.directions(
            origin=locations[0],
            destination=locations[-1],
            waypoints=waypoints_chunk,
            optimize_waypoints=True  # Key for route optimization
        )

        # Extract the route information from the response
        route.extend(directions_result[0]['legs'])

    return route

def write_sorted_locations_to_file(sorted_locations, output_file):
    """
    Writes sorted locations to a text file.
    """
    with open(output_file, 'w', encoding='utf-8') as file:
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
