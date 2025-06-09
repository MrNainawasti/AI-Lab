# WAP to display prime numbers from 1 to 100.
           
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

prime_numbers = []
print("Prime numbers from 1 to 100:")
for n in range(1, 101):
    if is_prime(n):
        prime_numbers.append(n)

print(prime_numbers)
