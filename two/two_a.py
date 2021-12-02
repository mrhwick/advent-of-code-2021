
from input import inputs

def navigate(inputs):
    pos = [0, 0]
    for instruction in inputs:
        short_instruction = instruction[0]
        amount = int(instruction[-1])
        if short_instruction == 'f':
            pos = [pos[0] + amount, pos[1]]
        if short_instruction == 'u':
            pos = [pos[0], pos[1] - amount]
        if short_instruction == 'd':
            pos = [pos[0], pos[1] + amount]
    
    return pos[0] * pos[1]

print(navigate(inputs))
