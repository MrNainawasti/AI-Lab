# WAP to calculate the factorial of an input number.

def fact(n):
    if n == 0:
        return 1
    else:
        return n * fact(n-1)
    
num = int(input("Enter any number: "))
factorial = fact(num)
print(f"factorail of {num} is {factorial} ")
