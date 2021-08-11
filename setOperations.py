from turtle import setundobuffer

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

#union
setUnion = setB.union(setC)
print("After Union : ", setUnion)
print('setB', setB)
print('setC', setC)
setUnionMultiple = setB.union(setA, setB, setC)
print("After Union Multiple: ", setUnionMultiple)

#intersection
print('Intersection: ',setB.intersection(setC))

#Difference
print('Difference: ', setB.difference(setC))

#Symmentric difference
print("Symmentric difference:", setB ^ setC)


print("Interjoint Result: ",setB.intersection(setC))
print('After Interjoint', setB)
print('After Interjoint', setC)

print("Interjoint Update Result: ", setC.intersection_update(setB))
print('After Interjointupdate', setB)
print('After Interjointupdate', setC)

#Giving iterable as an argument in the union() method
A={1,2,3,4,5}
#iterable is given as list
print (A.union([2,4,6]))#Output:{1, 2, 3, 4, 5, 6}

#iterable is given as tuple
print (A.union((2,4,6)))#Output:{1, 2, 3, 4, 5, 6}

#iterable is given as range object
print (A.union(range(5,10)))#Output:{1, 2, 3, 4, 5, 6, 7, 8, 9}

#iterable is given as a dictionary
print (A.union({'a':6,'b':7}))#Output:{1, 2, 3, 4, 5, 'b', 'a'}
