class A:
    num = 10

class B(A):
    pass

class C(A):
    num = 1

class D(B, C):

    def __init__(self):
        super(B).__init__(self)


#MRO method resolution order python

print(D.mro())
print(D.num)
