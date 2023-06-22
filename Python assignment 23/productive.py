class A:

    def __init__(self):

        self.m1 = 9

class X:

    def __init__(self):
        self.m3 = 7

class B(X, A):

    def __init__(self):
        super().__init__()

        self.m2 = 8


obj = B()


print(obj.m2)
print(obj.m3)