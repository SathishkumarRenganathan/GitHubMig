print('anitha')
a = 25
b = 25

c = a + b
d = 20
e = 15
print(c)
if (a < b):
    print('a value is less than b')
    if (a != d):
        print('both a and d values are same')
        d = 20
        if a != d:
            print('both value is not equal')
        elif(a > d):
            print('both value is not equal')
        else:
            print('both value are same')
            if (a > e):
                print('a value is greater than e')
            else:
                print('condtion failed')
    elif(a == b):
        print('condition true')
    else:
        print('condtion failed')

thulasi = "welcome "
anitha = 'to '
sathish = 'python'

str4 = thulasi+anitha+sathish
print(str4)

list_a = ['java','python','php','spring','machine learning']
print(list_a)
print(list_a[0])
print(list_a[4])

list_b = ['excel','powerpoint']
list_a = list_a+list_b
print(list_a)

tuple_a = ('welcome', 'python')
print(tuple_a)

tuple_b = ('world')
tuple_c = tuple_a+tuple_b
print(tuple_c)