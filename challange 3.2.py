"""
Implement a function called sort_students that takes a list of student objects as input and sorts the 
list based on their CGPA (cumulitive grade point average) in descending order.Each student object
has the following attributes: name (string) ,roll_number(string) , and cgpa (flaot). test the function
with different input of students.
"""

class student:

  def __init__(self,name,roll_number,cgpa):
    self.name = name
    self.roll_number = roll_number
    self.cgpa = cgpa


def sort_students(student_list):
  # sort the list of students in descending order of CGPA
  sorted_students = sorted(student_list,key=lambda student: student.cgpa,reverse=True)
 
  
  # syntax - lambda arg:exp                         
  return sorted_students


# example usage:
students=[
    student("karthik","A123",9.8),
    student("sunil","A124",8.9),
    student("meyyalagan","A125",9.1),
    student("naveen","A126",9.6),
]

sorted_students = sort_students(students)

# print the sorted list of students
for student in sorted_students:
  print("name: {}, roll number: {}, CGPA:{}".format(student.name,student.roll_number,student.cgpa))