# fare.py

from abc import ABC, abstractmethod

# Abstract Base Class
class FareCalculator(ABC):

    @abstractmethod
    def calculate_fare(self):
        pass

    @abstractmethod
    def display_fare_summary(self):
        pass


# Concrete Class 1
class RouteFare(FareCalculator):

    def __init__(self, distance):
        self.distance = distance
        self.rate = 10

    def calculate_fare(self):
        return self.distance * self.rate

    def display_fare_summary(self):
        print("----- Route Fare -----")
        print("Distance:", self.distance, "km")
        print("Fare:", self.calculate_fare())


# Concrete Class 2
class SpecialTripFare(FareCalculator):

    def __init__(self, distance):
        self.distance = distance
        self.rate = 15

    def calculate_fare(self):
        return self.distance * self.rate

    def display_fare_summary(self):
        print("----- Special Trip Fare -----")
        print("Distance:", self.distance, "km")
        print("Fare:", self.calculate_fare())
