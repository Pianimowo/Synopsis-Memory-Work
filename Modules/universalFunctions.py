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

    print(bitList)
    return bitList

    # decimal = 2**num
    # bitList = [[0 for x in range(num)] for y in range(decimal)]

    # for i in range (num):
    #     index = 0
    #     for j in range(int(decimal/(2**(i+1)))):
    #         index = (2**i)*((2*j)+1)
    #         for k in range(2**i):
    #             bitList[index+k][num-i-1] = 1

    
    
