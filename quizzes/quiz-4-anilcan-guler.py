def create_student(name,age):
    return (name, age)
def describe_student(student_tuple):
    name, age = student_tuple
    return print(f"Student {name} is {age} years old.")

student_name=input("Enter student's name: ")
student_age=int(input("Enter student's age: "))
student=create_student(student_name,student_age)
print(create_student(student_name,student_age))
describe_student(student)