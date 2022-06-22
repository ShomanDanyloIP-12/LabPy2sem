from classes import *
from func import *

m = int(input("Input amount of binary nums: "))
n = int(input("Input amount of octal nums: "))
print("\nBinary:")
binNums = inputNums(m, 2)
print("\nOctal:")
octNums = inputNums(n, 8)

print("\n")
print("Binary numbers: ")
outputNums(binNums)
print("Octal numbers: ")
outputNums(octNums)

incrementedBins = Increment(binNums)
decrementedOcts = Decrement(octNums)
print("\nIncremented binary: " + " ".join(map(str, incrementedBins)))
print("Decremented octs: " + " ".join(map(str, decrementedOcts)))
AllToDec = AllToDec(binNums, octNums)
print("All the numbers in decimal: " + " ".join(map(str, AllToDec)))
print("Minimal: " + str(min(AllToDec)))