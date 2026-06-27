from vehicles import Bus, MiniVan
from drivers import Driver

class TransportManager:

    def __init__(self, manager_name):
        self.manager_name = manager_name
        self.buses = []
        self.minivans = []
        self.drivers = []

    def add_bus(self, bus):
        self.buses.append(bus)

    def add_minivan(self, minivan):
        self.minivans.append(minivan)

    def add_driver(self, driver):
        self.drivers.append(driver)

    def display_all_vehicles(self):
        print("----- Vehicles -----")

        for vehicle in self.buses:
            vehicle.display_info()

        for vehicle in self.minivans:
            vehicle.display_info()

    def display_all_drivers(self):
        print("\n----- Drivers -----")

        for driver in self.drivers:
            driver.display_driver()

    # 👇 Paste search_vehicle() here
    def search_vehicle(self, vehicle_id):
        for bus in self.buses:
            if bus.vehicle_id == vehicle_id:
                print("\nBus Found:")
                bus.display_info()
                return

        for van in self.minivans:
            if van.vehicle_id == vehicle_id:
                print("\nMiniVan Found:")
                van.display_info()
                return

        print("Vehicle not found.")

    # 👇 Paste display_dashboard() here
    def display_dashboard(self):
        print("\n===== TRANSPORT DASHBOARD =====")
        print("Manager Name :", self.manager_name)
        print("Total Buses :", len(self.buses))
        print("Total MiniVans :", len(self.minivans))
        print("Total Drivers :", len(self.drivers))
        print("Total Vehicles :", len(self.buses) + len(self.minivans))