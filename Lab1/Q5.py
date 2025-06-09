# WAP to enter the marks of 10 students and display it.

def get_marks():

    marks = []
    for n in range(10):
        mark = float(input("Enter your mark:"))
        marks.append(mark)
    return marks

student_marks = get_marks()
print(student_marks)

