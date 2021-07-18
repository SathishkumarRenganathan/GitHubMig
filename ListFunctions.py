listA = ["python", "Django", "Spring", "Java", "python"]
setA = {"Samsung", "Apple", "OnePlus", "Mi", "Samsung"}
print(listA)
print(setA)
#append
listA.append("Ruby")
print('listA data',listA)
listB = listA.copy()

print('listB data', listB)

cnt = listA.count("python")
print('count val', cnt)

listA.extend(["C++", "C"])
print(listA)

print(listB.index("Java"))

listB.insert(3, "Foxpro")
print(listB)

listB.pop(3)
print(listB)
listB.remove("Java")
print(listB)

listB.reverse()
print(listB)