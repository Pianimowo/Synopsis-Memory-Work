import math
import numpy as np
from universalFunctions import compare
from universalFunctions import decoder

class OTP:
    def __init__(self, VDD, VPP, VRR):
        self.VDD = VDD
        self.VPP = VPP
        self.VRR = VRR

        # self.grid = [[0 for _ in range(size[0])] for _ in range(size[1])]

    def createGrid(self, rows, cols):
        self.memory = np.zeros((rows, cols), dtype=bool).astype(int)

    def loadGrid(self):
        self.memory = np.load("Data/memoryGrid.npy").astype(int)


    def edit(self, A, D, SEL, WE):
        length = math.log(self.memory.shape[0], 2)

        D = D*self.VDD

        row = decoder(A[0:int(length)])
        col = decoder(A[int(length):len(A)])

        if WE == 1:
            self.write(row, col, D, SEL)
        else:
            self.read(row, col, SEL)
        
        np.save("Data/memoryGrid.npy", self.memory)



    def write(self, row, col, D, SEL):
        if SEL > 0:
            self.memory[row, col] = D

    def read(self, row, col, SEL):
        if SEL > 0:
            out = self.memory[row, col]
            print(compare(out, self.VRR))

    def getGrid(self):
        memoryGrid = np.load("Data/memoryGrid.npy").astype(int)
        print(memoryGrid)

if __name__ == "__main__":
    test = OTP(5, 8, 0.4)
    test.loadGrid()
    test.edit([0, 0, 0, 1, 0, 1, 0], 1, 1, 0)
    test.getGrid()