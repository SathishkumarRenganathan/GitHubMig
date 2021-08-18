#Parent Class 1
class vehicle:
    def fuelType(self):
        print("Customer can choose fuelType..")

class twoWheeler(vehicle):
    def two_manufacturer(self):
        print("Ather")

class fourWheeler(twoWheeler):
    def four_manufacturer(self):
        print("tata")
vehicleObj = fourWheeler()
vehicleObj.four_manufacturer()
vehicleObj.two_manufacturer()
vehicleObj.fuelType()#Parent Class 1
class vehicle:
    def fuelType(self):
        print("Customer can choose fuelType..")

class twoWheeler(vehicle):
    def two_manufacturer(self):
        print("Ather")

class fourWheeler(twoWheeler):
    def four_manufacturer(self):
        print("tata")

class heavyVehicle(vehicle):
    def heavy_vehicle_manufacturer(self):
        print('TELCO')

vehicleObj = fourWheeler()
vehicleObj.four_manufacturer()
vehicleObj.two_manufacturer()
vehicleObj.fuelType()