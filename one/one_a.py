
from input import inputs

def count_increases(inputs):
    total = 0
    for i, measurement in enumerate(inputs):
        if i > 0 and measurement > inputs[i-1]:
            total += 1
    return total

print(count_increases(inputs))
