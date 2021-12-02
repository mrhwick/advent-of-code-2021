
from input import inputs

def navigate(inputs):
    position = [0, 0]
    pose = 0
    for instruction in inputs:
        short_instruction = instruction[0]
        amount = int(instruction[-1])
        if short_instruction == 'f':
            position = [position[0] + amount, position[1] + amount * pose]
        if short_instruction == 'u':
            pose -= amount
        if short_instruction == 'd':
            pose += amount
    
    return position[0] * position[1]

print(navigate(inputs))
