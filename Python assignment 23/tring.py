class Person:
    def __init__(self,rollno, id, yearofpassing):


        self.rollno = rollno

        self.id = id

        self.yearofpassing = yearofpassing



    def A(self):

        var = Person(14, "Student Tag", 2025)


        # Use the created instance
        print("")
        print(var.rollno)
        print("")
        print(var.id)
        print("")

        print(var.yearofpassing)


# Create an instance of the Person class

person_instacnce = Person(10, "12345", 2022)


person_instacnce.A()