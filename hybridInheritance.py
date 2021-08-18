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

class heavyVehicle(vehicle, fourWheeler):
    def heavy_vehicle_manufacturer(self):
        print('TELCO')
        super().four_manufacturer()
        four_manufacturer = super().four_manufacturer()
        heavy_manufacturer = 'tata'
        if(four_manufacturer == heavy_manufacturer):
            print('Both are same company')
        else:
            print('Both are not same company!')


vehicleObj = fourWheeler()
vehicleObj.four_manufacturer()
vehicleObj.two_manufacturer()
vehicleObj.fuelType()
heavyObj = heavyVehicle()
heavyObj.heavy_vehicle_manufacturer()