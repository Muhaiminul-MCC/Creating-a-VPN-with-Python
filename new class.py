# class and object

# classis a blueprint

# object is a blueprint conversion

# class
class student:

    def __init__(self, student_name, student_age):
        self.name = student_name
        self.age = student_age

# object
user_input1 = input("Enter your name: ")
user_input2 = input("How old are you: ")

s1 = student(user_input1, user_input2)
print(s1.name)
print(s1.age)