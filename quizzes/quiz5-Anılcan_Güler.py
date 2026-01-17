student_name=input("Please enter your name: ")
student_depatment=input("Please enter your department: ")
student_GPA=float(((input("Please enter your GPA: "))))
student_ID=int(input("Please enter your student ID: "))

student_info_dict={
    "name": student_name,
    "department": student_depatment,
    "GPA": student_GPA,
    "ID": student_ID
}

def describe_student(info_dict):
    print(f"student's name is {info_dict['name']} and he/she is studying in {info_dict['department']} department. His/Her GPA is {info_dict['GPA']} and student ID is {info_dict['ID']}.")
    
describe_student(student_info_dict)