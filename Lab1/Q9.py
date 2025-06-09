# WAP to sum all the items in a list.

def add(num_list):
    sum = 0
    for n in num_list:
        sum+= n
    return sum


numbers = [5, 4, 11, 13, 51]
sum = add(numbers)
print(sum)
