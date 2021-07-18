class person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def printName(self):
        print("My "+ self.firstname + " My "+self.lastname)

    def designation(self):
        print("Analyst")

#x=person("Welcome", "Python")
#x.printName()


#class student(person):
 #   pass

#x=student("Hello", "Welcome")
#x.printName()