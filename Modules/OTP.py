import math
import numpy as np
from universalFunctions import compare
from universalFunctions import decoder

class OTP:
    def __init__(self, VDD, VPP, VRR):
        self.VDD = VDD
        self.VPP = VPP
        self.VRR = VRR
        self.multipliers = None
        self.memory = None
        self.address_bits = None

        # self.grid = [[0 for _ in range(size[0])] for _ in range(size[1])]

    def createGrid(self, rows, cols):
        self.memory = np.zeros((rows, cols), dtype=np.float32)
        self.generateNoise()

    def loadGrid(self):
        self.memory = np.load("Data/memoryGrid.npy")
        self.generateNoise()

    def edit(self, A, D, SEL, WE):
        length = math.log(self.memory.shape[0], 2)

        D = D*self.VDD

        row = decoder(A[0:int(length)])
        col = decoder(A[int(length):len(A)])
        if WE == 1:
            self.write(row, col, D, SEL)
        else:
            self.read(row, col, SEL)

    def write(self, row, col, D, SEL):
        if SEL > 0:
            self.memory[row, col] = D * self.multipliers[row, col]

    def read(self, row, col, SEL):
        if SEL > 0:
            out = self.memory[row, col]
            print(compare(out, self.VRR))

    def generateNoise(self):
        self.multipliers = np.random.normal(loc=0.9, scale = 0.05, size = self.memory.shape)
        self.multipliers = np.clip(self.multipliers, 0.0, 1.0)

    def save(self):
        np.save("Data/memoryGrid.npy", self.memory)

    def getGrid(self):
        for row in self.memory:
            print(' '.join(f"{v:5.2f}" for v in row))

if __name__ == "__main__":
    test = OTP(5, 8, 0.4)
    test.loadGrid()
    test.edit([0, 0, 0, 0, 0, 0, 0, 0], 1, 1, 1)
    test.getGrid()
    test.save()