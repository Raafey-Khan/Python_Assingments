class School:
    # Class variable
    count = 0

    def __init__(self, name, location, num_students):
        self.name = name
        self.location = location
        self.num_students = num_students
        # Increment count class variable each time a new instance is created
        School.count += 1

# Create three instances of the School class
school1 = School("ABC School", "New York", 500)
school2 = School("XYZ School", "Chicago", 700)
school3 = School("PQR School", "Los Angeles", 600)

# Access and print the instance variables and class variable
print("School 1:")
print(f"Name: {school1.name}")
print(f"Location: {school1.location}")
print(f"Number of Students: {school1.num_students}")
print(f"Number of Schools: {School.count}")
print("-----------")
print("School 2:")
print(f"Name: {school2.name}")
print(f"Location: {school2.location}")
print(f"Number of Students: {school2.num_students}")
print(f"Number of Schools: {School.count}")
print("-----------")
print("School 3:")
print(f"Name: {school3.name}")
print(f"Location: {school3.location}")
print(f"Number of Students: {school3.num_students}")
print(f"Number of Schools: {School.count}")
