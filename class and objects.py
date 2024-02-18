class student:
    def __init__(self, student_name, student_age, student_location):
        self.name = student_name
        self.age = student_age
        self.location = student_location
        print("your information ....")

student_name = input("What is your name: ")
student_age = input("How old are you?: ")
student_location = input("where is your home?: ")
s1 = student(student_name, student_age, student_location)
print("Hi,", s1.name,".","You are", s1.age,"years old","and","you live in", s1.location, ":)")