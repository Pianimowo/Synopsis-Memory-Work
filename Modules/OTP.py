import math
import numpy as np
from universalFunctions import *

class OTP:
    def __init__(self, _VDD, _VPP, _VRR):
        self._VDD = _VDD
        self._VPP = _VPP
        self._VRR = _VRR
        self._A = None
        self._SEL = 0
        self._WE = 0
        self._dIn = 0
        self._dOut = ""
        self._IO = None
        self.multipliers = None
        self.memory = None
        self._suppress_update = False

    def createGrid(self, rows, cols):
        self.memory = np.zeros((rows, cols), dtype=np.float32)
        self.multipliers = np.random.normal(loc=50, scale = 10, size = self.memory.shape)
        np.save("Data/multipliers.npy", self.multipliers)
        # self.multipliers = np.clip(self.multipliers, 0.0, 1.0)
        print(self.multipliers)


    def loadGrid(self):
        self.memory = np.load("Data/memoryGrid.npy")
        self.multipliers = np.load("Data/multipliers.npy")
        print(self.multipliers)

    def _update_logic(self):
        if self._suppress_update:
            return
        if self._A is None or self.memory is None:
            return
        
        length = self.memory.shape[0]-1
        col = decoder(self._A)

        # print(self._D)

        if self._SEL == 1:
            if self._WE == 1:
                count = len(self._dIn)
                for i in range(length, length-count, -1):
                    self.write(col, i, self._dIn[count-1], self._SEL)
                    count -= 1
            else:
                temp = []
                for i in range(length+1):
                    temp.append(self.read(col, i, self._SEL))
                print(length)
                self._dOut = hex(decoder(temp))
                print(self._dOut)

    def write(self, row, col, _D, _SEL):
        if _SEL > 0:
            self.memory[row, col] = _D * self.multipliers[row, col]

    def read(self, row, col, _SEL):
        if _SEL > 0:
            out = self.memory[row, col]
            return compare(out, self._VRR)

    def save(self):
        np.save("Data/memoryGrid.npy", self.memory)

    def set_inputs(self, A=None, dIn=None, SEL=None, WE=None, IO = None):
        self._suppress_update = True  # prevent logic update during batch assignment
        if A is not None:
            self._A = A
        if dIn is not None:
            self._dIn = encoder(int(dIn, 16))
        if IO is not None:
            self._IO = IO
        if SEL is not None:
            self._SEL = SEL
        if WE is not None:
            self._WE = WE
        self._suppress_update = False
        self._update_logic() 

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
    for i in range(8):
        num = encoder(i)
        test.set_inputs(
        A = num,
        dIn = "23",
        SEL = 1,
        WE = 1,
        IO = 0,
    )
    test.getGrid()
    test.save()