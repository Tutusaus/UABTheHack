import webbrowser

def open_google_maps(start, destinations, end, start_from_current=False):
    base_url = "https://www.google.com/maps/dir/?api=1"
    
    # Format the origin, destination, and waypoints
    if start_from_current:
        origin = "origin=Current+Location"
    else:
        origin = f"origin={start.replace(' ', '+')}"
    
    destination = f"destination={end.replace(' ', '+')}"
    
    waypoints = ""
    if destinations:
        formatted_waypoints = [dest.replace(' ', '+') for dest in destinations]
        waypoints = f"&waypoints={'|'.join(formatted_waypoints)}"
    
    # Construct the full URL
    full_url = f"{base_url}&{origin}&{destination}{waypoints}"

    # Open the web browser with the constructed URL
    webbrowser.open(full_url)

def load_destinations(file_path):
    with open(file_path, 'r') as file:
        destinations = [line.strip() for line in file.readlines()]
    return destinations

if __name__ == "__main__":
    # Load destinations from the file
    file_path = 'sorted_locations.txt'
    destinations = load_destinations(file_path)

    # Prompt the user to choose the starting location option
    start_option = input("Do you want to start the route from your current location? (yes/no): ").lower()
    if start_option == "yes":
        start_from_current = True
        start = None  # No need for a starting point if starting from current location
    else:
        start_from_current = False
        start = input("Enter the starting location: ")
    
    # Prompt the user to enter the ending location
    end = input("Enter the ending location: ")

    open_google_maps(start, destinations, end, start_from_current)
