# WAP to sort the list {5, 4, 11, 13, 51}.

def sort(numbers):
    sorted_list = []
    for index in range(len(numbers)-1):
        if numbers[index-1] < numbers[index]:
            sorted_list.append(numbers[index-1])
    return sorted_list



numbers = [5, 4, 11, 13, 51]

# numbers.sort()
# print(numbers)

sorted_list = sort(numbers)
print(sorted_list)

