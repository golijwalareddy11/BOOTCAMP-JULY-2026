from transport_manager import TransportManager
from vehicles import Bus, MiniVan
from drivers import Driver
from fare import RouteFare, SpecialTripFare



def display_main_menu():
    print("\n" + "=" * 55)
    print(" ACE Engineering College Transportation Portal ")
    print("=" * 55)
    print("1. Add Bus")
    print("2. Add MiniVan")
    print("3. Add Driver")
    print("4. Display All Vehicles")
    print("5. Display All Drivers")
    print("6. Route Fare Calculator")
    print("7. Special Trip Fare Calculator")
    print("8. Search Vehicle")
    print("9. Display Dashboard")
    print("0. Exit")



def main():

    manager = TransportManager("Mr. Ramesh")

    while True:
        display_main_menu()
        choice = input("Enter your choice: ").strip()

        if choice == "1":

            print("\n[ADD BUS]")
            vehicle_id = input("Vehicle ID: ")
            capacity = int(input("Capacity: "))
            route_number = input("Route Number: ")
            ac = input("Has AC? (yes/no): ").lower() == "yes"

            if Bus.validate_vehicle_id(vehicle_id):
                bus = Bus(vehicle_id, capacity, route_number, ac)
                manager.add_bus(bus)
                print("Bus added successfully.")
            else:
                print("Invalid Vehicle ID!")

        elif choice == "2":

            print("\n[ADD MINIVAN]")
            vehicle_id = input("Vehicle ID: ")
            capacity = int(input("Capacity: "))
            purpose = input("Trip Purpose: ")

            if MiniVan.validate_vehicle_id(vehicle_id):
                van = MiniVan(vehicle_id, capacity, purpose)
                manager.add_minivan(van)
                print("MiniVan added successfully.")
            else:
                print("Invalid Vehicle ID!")

        elif choice == "3":

            print("\n[ADD DRIVER]")
            driver_id = input("Driver ID: ")
            name = input("Driver Name: ")
            license_no = input("License Number: ")
            contact = input("Contact: ")

            driver = Driver(driver_id, name, license_no, contact)
            manager.add_driver(driver)

            print("Driver added successfully.")

        elif choice == "4":

            manager.display_all_vehicles()

        elif choice == "5":

            manager.display_all_drivers()

        elif choice == "6":

            print("\n[ROUTE FARE CALCULATOR]")

            distance = float(input("Distance (km): "))

            fare = RouteFare(distance)

            fare.display_fare_summary()

        elif choice == "7":

            print("\n[SPECIAL TRIP FARE CALCULATOR]")

            distance = float(input("Distance (km): "))

            fare = SpecialTripFare(distance)

            fare.display_fare_summary()

        elif choice == "8":

            vehicle_id = input("Enter Vehicle ID: ")
            manager.search_vehicle(vehicle_id)

        elif choice == "9":

            manager.display_dashboard()

        elif choice == "0":

            print("\nThank you for using ACE Transportation Portal!")
            print("Goodbye!\n")
            break

        else:

            print("Invalid Choice!")



if __name__ == "__main__":
    main()