from itertools import product

def decoder (binary):
    decimal = 0
    digit = 0
    counter = 0

    for i in reversed(binary):
        digit = (2**counter) * i
        decimal += digit
        counter += 1

    return decimal

def binaryInputs (num):
    bitList = [list(bits) for bits in product([0, 1], repeat=num)]
    return bitList

def compare(input, VRR):
    if input >= VRR:
        return 1
    else:
        return 0
    