# WAP to check if an input number is odd or even


def odd_even_check(n):
    if n % 2 == 0:
        return True




user_input = int(input("Enter any number: "))

if odd_even_check(user_input):
    print("The number is even.")
else:
    print("The number is odd.")
