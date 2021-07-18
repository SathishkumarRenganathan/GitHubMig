tupleA = (12,12,15,19,90)
print(len(tupleA))
#cnt = tupleA.count(12)
#print(cnt)
print(tupleA.count(12))
print(tupleA.index(19))

setA = {"Hello", "Welcome.", "Python", "to", "Python"}
print(setA)

setB = {"Hello", "Welcome", "Python"}
setC = {"Morning", "Good", "Python"}
print("Interjoint Result: ",setB.intersection(setC))
print('After Interjoint', setB)
print('After Interjoint', setC)

print("Interjoint Update Result: ", setC.intersection_update(setB))
print('After Interjointupdate', setB)
print('After Interjointupdate', setC)
