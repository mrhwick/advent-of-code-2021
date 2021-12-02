
from input import inputs

def count_increases_window(inputs):
    total = 0
    for i in range(len(inputs) + 1):
        if i <= 3:
            continue

        first_window = sum(inputs[i-4:i-1]) 
        second_window = sum(inputs[i-3:i]) 

        if first_window < second_window:
            total += 1
            
    return total


print(count_increases_window(inputs))
