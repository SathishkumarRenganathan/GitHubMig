class hello:

    #def printmsg(self):
     #   print("Hi!!!")
    #printmsg()


    def calc(self):
        a = 10
        b = 10
        c = a + b
        return c

    def addCalc(self, c):
        d = c + 20
        print(d)

hObj = hello()
c = hObj.calc()
hObj.addCalc(c)
