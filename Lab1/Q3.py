# WAP to calculate sum, diff, product and quotient between two input numbers using a single function.

def calculator(n1, n2):
    sum = n1 + n2
    diff = n1 - n2
    prod  = n1 * n2
    quotient = n1 / n2
    results = (sum, diff, prod, quotient)
    return results


num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
answer = calculator(num1, num2)
print(answer)



