def decoder (binary):
    decimal = 0
    digit = 0
    counter = 0

    for i in reversed(binary):
        digit = (2**counter) * i
        decimal += digit
        counter += 1

    return decimal