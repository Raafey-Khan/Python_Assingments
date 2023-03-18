class user:
    def __init__(self,greet):
        self.greet = greet


    def show(self):
        print(f"Hello {self.greet} nice to see your typing")


a = user(input("Enter your name:"))

a.show()
