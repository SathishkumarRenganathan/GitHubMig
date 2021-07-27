#parent class
class dieselCar:
    fuel = 'diesel'
    def gearType(self):
        print('Automatic')
    def carType(self):
        print('SUV')


#sub class
class petrolCar(dieselCar):
    fuel = 'petrol'
    def gearType(self):
        print('Manual')
    def carCategory(self):
        print('Luxury')

dObj = dieselCar()
pObj = petrolCar()

dObj.gearType()
pObj.gearType()

dObj.carType()

pObj.carType()
pObj.carCategory()

print(pObj.fuel)

