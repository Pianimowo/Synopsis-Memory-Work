class resistorLadder:
    def __init__(self, input_voltage, ground, control):
        self.input_voltage = input_voltage
        self.ground = ground
        self.control = control


        from universalFunctions import decoder
        

        self.newcontrol = decoder(self.control)

        size_of_gap = (self.input_voltage-self.ground)/float(2**len(self.control))


        self.output = self.ground + (size_of_gap*self.newcontrol + size_of_gap/2)

    def get_output(self):
        print(self.output)


if __name__ == "__main__":
    from universalFunctions import binaryInputs
    list = binaryInputs(4)
    for i in range(len(list)):
        print(list[i])     
        blackBoxTest = resistorLadder(4, 0, list[i])
        blackBoxTest.get_output()