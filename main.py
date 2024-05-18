import webbrowser

def open_google_maps(start, destinations, end):
    base_url = "https://www.google.com/maps/dir/?api=1"
    
    # Format the origin, destination, and waypoints
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
    file_path = 'destinations.txt'
    destinations = load_destinations(file_path)

    # Prompt the user to enter the starting and ending locations
    start = input("Enter the starting location: ")
    end = input("Enter the ending location: ")

    open_google_maps(start, destinations, end)
