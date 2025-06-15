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
        self._suppress_update = False

    def createGrid(self, rows, cols):
        self.memory = np.zeros((rows, cols), dtype=np.float32)
        self.generateNoise()

    def loadGrid(self):
        self.memory = np.load("Data/memoryGrid.npy")
        self.generateNoise()

    def _update_logic(self):
        if self._suppress_update:
            return
        if self._A is None or self.memory is None:
            return
        
        length = math.log2(self.memory.shape[0])
        row = decoder(self._A[int(length):len(self._A)])
        col = decoder(self._A[0:int(length)])

        # print(self._D)

        if self._SEL == 1:
            if self._WE == 1:
                self._D = self._D*self._VDD
                self.write(row, col, self._D, self._SEL)
            else:
                self.read(row, col, self._SEL)

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
        # print(self.multipliers)

    def save(self):
        np.save("Data/memoryGrid.npy", self.memory)

    def set_inputs(self, A=None, D=None, SEL=None, WE=None):
        self._suppress_update = True  # prevent logic update during batch assignment
        if A is not None:
            self._A = A
        if D is not None:
            self._D = D
        if SEL is not None:
            self._SEL = SEL
        if WE is not None:
            self._WE = WE
        self._suppress_update = False
        self._update_logic()  # 


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
        self._update_logic()
    
    @property
    def A(self):
        return self._A
    
    @A.setter
    def A(self, value):
        self._A = value
        self._update_logic()
    
    @property
    def D(self):
        return self._D
    
    @D.setter
    def D(self, value):
        self._D = value
        self._update_logic()
    
    @property
    def SEL(self):
        return self._SEL
    
    @SEL.setter
    def SEL(self, value):
        self._SEL = value
        self._update_logic()
    
    @property
    def WE(self):
        return self._WE
    
    @WE.setter
    def WE(self, value):
        self._WE = value
        self._update_logic()

    def getGrid(self):
        for row in self.memory:
            print(' '.join(f"{v:5.2f}" for v in row))

if __name__ == "__main__":
    test = OTP(5, 8, 0.4)
    test.createGrid(8, 8)
    test.set_inputs(
        A = [0, 0, 1, 0, 1, 0],
        SEL = 1,
        D = 1,
        WE = 1
    )
    test.getGrid()
    test.save()