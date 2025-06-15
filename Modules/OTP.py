import math
import numpy as np
from universalFunctions import compare
from universalFunctions import decoder

class OTP:
    def __init__(self, size, VDD, VPP, VRR):
        self.VDD = VDD
        self.VPP = VPP
        self.VRR = VRR
        self.size = size

        self.len = int(math.log(self.size[0], 2))
        self.wid = int(math.log(self.size[1], 2))

        self.grid = [[0 for _ in range(size[0])] for _ in range(size[1])]

    # def createGrid(self, A, D, SEL, WE):


    def edit(self, A, D, SEL, WE):

        D = D*self.VDD

        row = decoder(A[0:int(self.len)])
        col = decoder(A[int(self.len):len(A)])

        if WE == 1:
            self.write(row, col, D, SEL)
        else:
            self.read(row, col, SEL)

        for i in self.grid:
            print(i)

    def write(self, row, col, D, SEL):
        if SEL > 0:
            with open("Data\memoryGrid.txt","w") as f:
                f.write("write")
            self.grid[row][col] = D

    def read(self, row, col, SEL):
        if SEL > 0:
            out = compare(self.grid[row][col], self.VRR)
            print(out)


    def test(self):
        print("test")

if __name__ == "__main__":
    test = OTP([8, 8], 5, 8, 0.4)
    test.edit([0, 0, 1, 0, 1, 0], 1, 1, 1)