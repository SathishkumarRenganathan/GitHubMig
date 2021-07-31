from functools import reduce

intVal = lambda x: x + 5
print(intVal(10))

#using filter method
seq=[12,45,2,3,5,9,4,7]
result = filter(lambda seq: seq>5, seq)
print(list(result))

#using map method
seqMap=[12,45,2,3,5,9,4,7]
resultMap = map(lambda  seq : seq*2, seq)
print(list(resultMap))

#using reduce method
seq = [1,3,5]
resultReduce = reduce(lambda x, y: x*y, seq)
print(resultReduce)