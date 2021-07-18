aNum = int(input("Enter a value: "))
bNum = int(input("Enter b Value: "))
try:
    c = aNum/bNum
    print(c)
except ZeroDivisionError:
    print('Arithmatic Exception has occurred')
except NameError:
    print('value not declared')
except BaseException:
    print("Error Occurred")
finally:
    del c
    del aNum
    del bNum
    print('aNum Val:', aNum)

mtcList = [12,15,17,59,66,67,78,15]
print(type(mtcList))
searchRoute = 66
#print(type(searchRoute))
for an in mtcList:
    if(an == searchRoute):
        print("Route No Correct...")
        break
    else:
        print("Specified Route Bus not orginated from Tambaram")