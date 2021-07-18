class ListOpr:
    def listDeclare(self):
        listA = ["Java", "Android", "Kotlin"]
        print(listA)

    def listOperations(self):
        listB = ["Python", "Django", "Data Science", "Machine Learning"]
        print("Before Append: " , listB)
        listB.append("AI")
        print("After Append: ", listB)
        listB.append("Django")
        print("Check List allows Duplicates After Append: ", listB)
        listB.insert(3,"SpringBoot")
        print("After Insert Operation:", listB)
        size = listB.count("Django")
        print("List Count: ", size)
        listB.pop(3)
        print("After the POP Operation: ", listB)
        listB.remove("AI")
        print("After the remove Element in the List:", listB)

listObj = ListOpr();
listObj.listDeclare()
listObj.listOperations()