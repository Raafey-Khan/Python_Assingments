class User:
    def __init__(self, username, email, password, age):
        self.username = username
        self.email = email
        self.password = password
        self.age = age

user1 = User("johndoe", "johndoe@example.com", "password", 25)
print(user1.__dict__)  # output: {'username': 'johndoe', 'email': 'johndoe@example.com', 'password': 'password', 'age': 25}

del user1.age

print(user1.__dict__)  # output: {'username': 'johndoe', 'email': 'johndoe@example.com', 'password': 'password'}
