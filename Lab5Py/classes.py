from abc import ABC, abstractmethod
from classfunc import *

class TIntNumber(ABC):
    def __init__(self, value=0, base=10):
        self.__value = value
        self.__base = base

    @property
    def getBase(self):
        return self.__base

    @property
    def getValue(self):
        return self.__value

    @getValue.setter
    def getValue(self, val):
        self.__value = val

    @abstractmethod
    def __pos__(self):
        pass

    @abstractmethod
    def __neg__(self):
        pass

    @abstractmethod
    def convertTo10(self, base):
        return convertToDec(self.__value, base)


class TIntNumber2(TIntNumber):
    def __init__(self, value = 0):
        super().__init__(value, 2)
    def __pos__(self):
        increment = TIntNumber2(convertFromDec(convertToDec(self.getValue, 2) + 1, 2))
        self.getValue = increment.getValue
    def __neg__(self):
        decrement = TIntNumber2(convertFromDec(convertToDec(self.getValue, 2) - 1, 2))
        self.getValue = decrement.getValue
    def convertTo10(self, base = 2):
        return super().convertTo10(base)



class TIntNumber8(TIntNumber):
    def __init__(self, value=0):
        super().__init__(value, 8)

    def __pos__(self):
        increment = TIntNumber8(convertFromDec(convertToDec(self.getValue, 8) + 1, 8))
        self.getValue = increment.getValue

    def __neg__(self):
        decrement = TIntNumber8(convertFromDec(convertToDec(self.getValue, 8) - 1, 8))
        self.getValue = decrement.getValue

    def convertTo10(self, base=8):
        return super().convertTo10(base)
