import webbrowser
from urllib.parse import quote

def open_google_maps(start, destinations, end, start_from_current=False):
    base_url = "https://www.google.com/maps/dir/?api=1"
    
    # Format the origin, destination, and waypoints
    if start_from_current:
        origin = "origin=Current+Location"
    else:
        origin = f"origin={quote(start)}"
    
    destination = f"destination={quote(end)}"
    
    waypoints = ""
    if destinations:
        formatted_waypoints = [quote(dest) for dest in destinations]
        waypoints = "&waypoints=" + '|'.join(formatted_waypoints)
    
    # Construct the full URL
    full_url = f"{base_url}&{origin}&{destination}{waypoints}"

    # Open the web browser with the constructed URL
    webbrowser.open(full_url)

def load_destinations(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        destinations = [line.strip() for line in file.readlines()]
    return destinations

if __name__ == "__main__":
    # Load destinations from the file
    file_path = 'sorted_locations.txt'
    destinations = load_destinations(file_path)

    # Assign the first and last lines to start and end
    start = destinations[0]
    end = destinations[-1]

    # Use the remaining lines as waypoints
    waypoints = destinations[1:-1]

    open_google_maps(start, waypoints, end)
