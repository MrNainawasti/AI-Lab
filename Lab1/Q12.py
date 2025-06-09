# WAP to find the sum of all items in a dictionary

# Input = {'a': 100, 'b':200, 'c':300}
Input = {'x': 25, 'y':18, 'z':45}

def sum(dict):
    sum = 0
    for key in dict:
        sum+= dict[key]
    return sum   



sum = sum(Input)
print(sum)
