from person import person
class student(person):
    def __init__(self, fname, lname,year):
        super().__init__(fname,lname)
        self.gratuationYear = year

x = student("Anitha", "Thulasiram",2019)
print(x.firstname, x.lastname, x.gratuationYear)
x.printName()