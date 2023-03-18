class User:
    def __init__(self, username, email, password, age=18, is_active=True):
        self.username = username
        self.email = email
        self.password = password
        self.age = age
        self.is_active = is_active

user1 = User("johndoe", "johndoe@example.com", "password")
print(user1.username)  # output: johndoe
print(user1.age)  # output: 18 (default value)

user2 = User("janedoe", "janedoe@example.com", "password", 25, False)
print(user2.username)  # output: janedoe
print(user2.age)  # output: 25
print(user2.is_active)  # output: False
