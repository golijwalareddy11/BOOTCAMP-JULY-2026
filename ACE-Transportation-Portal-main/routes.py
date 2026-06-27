# routes.py
route_1_stops = ["College Gate", "RTC Cross", "Miyapur"]
stop_coordinates = (17.4939, 78.3996)
registered_pass_ids = {"ACE001", "ACE002", "ACE003"}
bus_fleet = {
    "bus_no": "TS28Z1234",
    "capacity": 50,
    "driver": "Ramesh"
}
def display_route_stops(route_stops):
    print("\nRoute Stops:")
    for stop in route_stops:
        print(stop)
# Add a new stop to an existing route

def add_stop(route_stops, new_stop):
    route_stops.append(new_stop)
    print(f"{new_stop} added successfully.")
# Register a new student pass ID

def register_student_pass(pass_set, student_id):
    if student_id not in pass_set:
        pass_set.add(student_id)
        print(f"{student_id} registered successfully.")
    else:
        print("Student ID already exists.")
# Display all bus fleet details

def display_bus_details(bus_dict):
    print("\nBus Details:")
    for key, value in bus_dict.items():
        print(f"{key}: {value}")


