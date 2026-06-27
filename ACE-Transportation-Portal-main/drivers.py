# drivers.py

class Driver:
    def __init__(self, driver_id, name, license_no, contact):
        self.driver_id = driver_id
        self.name = name
        self._license_no = license_no
        self._contact = contact

    # Getter
    @property
    def license_no(self):
        return self._license_no

    # Setter
    @license_no.setter
    def license_no(self, new_license):
        if len(new_license) >= 8:
            self._license_no = new_license
            print("License updated successfully.")
        else:
            print("Invalid license number.")

    # Getter for contact
    @property
    def contact(self):
        return self._contact

    # Deleter
    @contact.deleter
    def contact(self):
        print("Driver contact removed.")
        del self._contact

    # Display Driver Details
    def display_driver(self):
        print("Driver ID      :", self.driver_id)
        print("Driver Name    :", self.name)
        print("License Number :", self.license_no)
        if hasattr(self, "_contact"):
            print("Contact        :", self._contact)
        else:
            print("Contact        : Removed")
