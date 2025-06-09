# WAP program to get the largest number from a list.

def check_num(num_list):
    a = 0
    for n in num_list:
        if n > a:
            a = n
    return a
    
numbers = [5, 4, 11, 13, 51]
largest_number = check_num(numbers)
print(largest_number)
