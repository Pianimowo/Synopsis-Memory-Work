class blackBox:
    def __init__(self, input_voltage, ground, control):
        self.input_voltage = input_voltage
        self.ground = ground
        self.control = control


        from Modules.universalFunctions import decoder

        self.newcontrol = decoder(self.control)

        size_of_gap = (self.input_voltage-self.ground)/float(2**len(self.control))


        self.output = self.ground + (size_of_gap*self.newcontrol)

    def get_output(self):
        print(self.output)




def test():
    print("Hello")





if __name__ == "__main__":
    blackBoxTest = blackBox(4, 0, [0, 1, 1, 1])
    blackBoxTest.get_output()