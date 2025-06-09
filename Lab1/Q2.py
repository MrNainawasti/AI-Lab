# WAP to input the percentage and display the division
# >=80 →  Distinction
# >=65 →  First Division
# >=55 →  Second Division
# >=40 →  Third Division
# <40  →  Fail

def division_check(percent):
    if percent >= 80:
        return "Distinction"
    elif percent >= 60:
        return "First Division"
    elif percent >= 55:
        return "Second Division"
    elif percent >= 40:
        return "Third Division"
    else:
        return "Fail"

    

user_percentage = float(input("Enter your percentage: "))
result = division_check(user_percentage)
print(result)
