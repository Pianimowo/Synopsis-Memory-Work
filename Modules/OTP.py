import math

class OTP:
    def __init__(self, size, VDD, VPP, VRR):
        self.VDD = VDD
        self.VPP = VPP
        self.VRR = VRR
        self.size = size


        
        self.len = int(math.log(self.size[0], 2))
        self.wid = int(math.log(self.size[1], 2))

        self.grid = [[0 for _ in range(size[0])] for _ in range(size[1])]

    def run(self, A, D, SEL, WE):
        from universalFunctions import compare
        from universalFunctions import decoder

        compD = compare(D, self.VRR)
        compSEL = compare(SEL, self.VRR)
        compWE = compare(WE, self.VRR)

        row = decoder(A[0:int(self.len)])
        col = decoder(A[int(self.len):len(A)])

        if compWE == 1:
            self.write(row, col, compD, compSEL)
        else:
            self.read(row, col, compSEL)

        for i in self.grid:
            print(i)

    def write(self, row, col, D, SEL):
        if SEL > 0:
            self.grid[row][col] = D

    def read(self, row, col, SEL):
        if SEL > 0:
            out = self.grid[row][col]
            print(out)


    def test(self):
        print("test")

if __name__ == "__main__":
    test = OTP([8, 8], 5, 8, 0.4)
    test.run([0, 0, 1, 0, 1, 0], 5, 5, 5)