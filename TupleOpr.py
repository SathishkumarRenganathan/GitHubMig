from ListOpr import listImport

class TupleOpr:
    def tupleFns(self):
        tupleA = ("Java", "Python", "Data Structure")
        tupleB = ("AI", "C++")
        listA = ["Android", "DevOps", "SAP-ABAP"]
        print(tupleA)
        print(listA)
        tupleC = tuple(listA)
        print(tupleC)
        print("Tuple Count: ", tupleA.count("Java"))
        print("Tuple Index: ",tupleA.index("Data Structure"))
        print(tupleA.__contains__("AI"))
        tupleA.__add__(tupleB)
        print(tupleA)
tupleObj = TupleOpr()
tupleObj.tupleFns()
listImport.listDeclare()