import math
import numpy as np
from universalFunctions import compare
from universalFunctions import decoder

class OTP:
    def __init__(self, _VDD, _VPP, _VRR):
        self._VDD = _VDD
        self._VPP = _VPP
        self._VRR = _VRR
        self._A = None
        self._D = 0
        self._SEL = 0
        self._WE = 0
        self.multipliers = None
        self.memory = None

    def createGrid(self, rows, cols):
        self.memory = np.zeros((rows, cols), dtype=np.float32)
        self.generateNoise()

    def loadGrid(self):
        self.memory = np.load("Data/memoryGrid.npy")
        self.generateNoise()

    def _update_logic(self):
        return

    def edit(self, _A, _D, _SEL, _WE):
        length = math.log(self.memory.shape[0], 2)

        _D = _D*self._VDD

        row = decoder(_A[int(length):len(_A)])
        col = decoder(_A[0:int(length)])

        if _WE == 1:
            self.write(row, col, _D, _SEL)
        else:
            self.read(row, col, _SEL)

    def write(self, row, col, _D, _SEL):
        if _SEL > 0:
            self.memory[row, col] = _D * self.multipliers[row, col]

    def read(self, row, col, _SEL):
        if _SEL > 0:
            out = self.memory[row, col]
            print(compare(out, self._VRR))

    def generateNoise(self):
        self.multipliers = np.random.normal(loc=1.0, scale = 0.05, size = self.memory.shape)
        # self.multipliers = np.clip(self.multipliers, 0.0, 1.0)
        print(self.multipliers)

    def save(self):
        np.save("Data/memoryGrid.npy", self.memory)

    
    @property
    def VDD(self):
        return self._VDD
    
    @VDD.setter
    def VDD(self, value):
        self._VDD = value
        self._update_logic()
    
    @property
    def VPP(self):
        return self._VPP
    
    @VPP.setter
    def VPP(self, value):
        self._VPP = value
        self._update_logic()
    
    @property
    def VRR(self):
        return self._VRR
    
    @VRR.setter
    def VRR(self, value):
        self._VRR = value
        self._update_logic
    
    @property
    def A(self):
        return self._A
    
    @A.setter
    def A(self, value):
        self._A = value
        self._update_logic
    
    @property
    def D(self):
        return self._D
    
    @D.setter
    def D(self, value):
        self._D = value
        self._update_logic
    
    @property
    def SEL(self):
        return self._SEL
    
    @SEL.setter
    def SEL(self, value):
        self._SEL = value
        self._update_logic
    
    @property
    def WE(self):
        return self._WE
    
    @WE.setter
    def WE(self, value):
        self._WE = value
        self._update_logic

    def getGrid(self):
        for row in self.memory:
            print(' '.join(f"{v:5.2f}" for v in row))

if __name__ == "__main__":
    test = OTP(5, 8, 0.4)
    test.createGrid(8, 8)
    test.edit([0, 0, 1, 0, 1, 0], 1, 1, 1)
    test.getGrid()
    test.save()