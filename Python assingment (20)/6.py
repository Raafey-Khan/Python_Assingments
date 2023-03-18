class User:
    def __init__(self, username, email, password, age):
        self.username = username
        self.email = email
        self.password = password
        self.age = age

user1 = User("johndoe", "johndoe@example.com", "password", 25)
user2 = User("janedoe", "janedoe@example.com", "password", 30)
user3 = User("bobdoe", "bobdoe@example.com", "password", 20)

youngest_user = user1

if user2.age < youngest_user.age:
    youngest_user = user2

if user3.age < youngest_user.age:
    youngest_user = user3

print("The youngest user is", youngest_user.username, "who is", youngest_user.age, "years old.")
