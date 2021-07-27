#parent class 1
class A:
    val1 = 0
    def fun1(self):
        print(self.val1)

#parent class2
class B:
    val2 = 0
    def fun2(self):
        print(self.val2)

#child class
class C(A, B):
    def fun3(self):
        print("Inheritance Implementation")

obj = C()
obj.val1 = 10
obj.val2 = 20
obj.fun3()
print(obj.val1)
print(obj.val2)
