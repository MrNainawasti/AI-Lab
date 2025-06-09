# Representation of the graph using a dictionary
graph = {
    'Biratnagar': {'Itahari': 22, 'Rangeli': 25, 'Biratchowk': 30},
    'Itahari': {'Biratnagar': 22, 'Biratchowk': 11, 'Dharan': 20},
    'Biratchowk': {'Itahari': 11, 'Kanepokhari': 10, 'Biratnagar': 30},
    'Dharan': {'Itahari': 20},
    'Rangeli': {'Biratnagar': 25, 'Kanepokhari': 25},
    'Kanepokhari': {'Rangeli': 25, 'Biratchowk': 10, 'Urlabari': 12},
    'Urlabari': {'Kanepokhari': 12, 'Damak': 6},
    'Damak': {'Urlabari': 6}
}

# Printing the graph
for location, connections in graph.items():
    print(f"{location} is connected to:")
    for connected_location, distance in connections.items():
        print(f"  - {connected_location} with a distance of {distance} km")
