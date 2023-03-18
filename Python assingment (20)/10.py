class Employee:
    def __init__(self, empid, name, salary):
        self.empid = empid
        self.name = name
        self.salary = salary

    def input_fields(self):
        self.empid = input("Enter Employee ID: ")
        self.name = input("Enter Employee Name: ")
        self.salary = input("Enter Employee Salary: ")

    def display_fields(self):
        print("Employee ID: ", self.empid)
        print("Employee Name: ", self.name)
        print("Employee Salary: ", self.salary)


# Create an instance of Employee class
emp1 = Employee("E101", "John Doe", 50000)

# Call display_fields method to display initial values
emp1.display_fields()

# Call input_fields method to update values
emp1.input_fields()

# Call display_fields method again to display updated values
emp1.display_fields()
