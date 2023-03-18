class User:

    def __init__(self,obj1,obj2):

        self.obj1 = obj1

        self.obj2 = obj2


    def show(self):
        print(f"First value {self.obj1}")
        print(f"Second value {self.obj2}")

        

        
printer = User(10,20)

printer.show()

