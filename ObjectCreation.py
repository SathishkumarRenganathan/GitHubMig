class calc:
    def add(self):
        c=12 + 15
        print(c)

    def addParam(self, a, b):
        c=a+b
        print("Addition Val is : ", c)
aVal = int(input("Enter the a val: "))
bVal = int(input("Enter the b val: "))
calcObj = calc()
calcObj.add()
calcObj.addParam(aVal,bVal)