class student:
    def __init__(self, student_name, student_age, student_location):
        self.name = student_name
        self.age = student_age
        self.location = student_location
        print("your information ....")

student_list = []

student_num = int(input("Enter number of student: "))
for i in range(student_num):
    student_name = input("What is your name: ")
    student_age = int(input("How old are you?: "))
    student_location = input("where is your home?: ")
    s = student(student_name, student_age, student_location)
    student_list.append(s)

print(student_list[0].name, student_list[0].age, student_list[0].location)
print(student_list[1].name, student_list[1].age, student_list[1].location)

print(type(student_list))
print(type(student_list[0]), type(student_list[1]))
print(type(student_list[0].name), type(student_list[0].age), type(student_list[0].location))

"""
s1 = student(student_name, student_age, student_location)
print("Hi,", s1.name,".","You are", s1.age,"years old","and","you live in", s1.location, ":)")
"""