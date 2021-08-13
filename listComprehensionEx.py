'''It is easy way to create the list from a existing list, tuple, dictionary, set, strings
It is very fast for processing the list comparing then for loop processing
newList = [ expression(element) for element in oldList if condition ]
'''

num =[]
for x in range(10):
    if x%2 == 0:
        num.append(x)
print(num)

#using list comprehension
num = [x for x in range(10) if x%2 == 0]
print(num)

square = [x*x for x in range(5)]
print(square)

strList = ['Hello','Welcome', 'Python', 'Data Science', 'Block Chain']
list = [str for str in strList if 'n' in str]
print(list)

n1 = [1,2,3]
n2 = [4,5,6]
n1n2 = [(x,y) for x in n1 for y in n2]
print(n1n2)

outList = [str(i) if i%2 == 0 else str(i)+"=Odd" for i in range(20)]
print(outList)