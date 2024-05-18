import googlemaps

# Replace with your Google Maps API key
API_KEY = 'AIzaSyD51o19sz6638p2WjiAiLOpHPWXkCgXq6c'
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

    # 3. Print route details
    print_route_details(route)

    # 4. Extract sorted locations from the route
    sorted_locations = [leg['start_address'] for leg in route]
    sorted_locations.append(route[-1]['end_address'])

    # 5. Write sorted locations to file
    write_sorted_locations_to_file(sorted_locations, 'sorted_locations.txt')
