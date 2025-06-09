# Write a Python program to create a person class. Include attributes like name, country and date of
# birth. Implement a method to determine the person's age.

from datetime import date

class Person:

    def __init__(self, name, country, dob):
        self.name = name
        self.country = country
        self.date_of_birth = dob


    def calculate_age(self):
        today = date.today()
        age = today.year - self.date_of_birth[0]
        return age



name = input("Enter your name: ")
country = input("Enter your country: ")

date_of_birth = input("Enter your date of birth(yy-mm-dd): ")
dob = tuple(int(item) for item in date_of_birth.split("-"))

person_1 = Person(name, country, dob)

person_1_age = person_1.calculate_age()
print(person_1_age)



