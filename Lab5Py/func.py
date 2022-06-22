from classes import *


def isInputCorrect(num, base):
    while num:
        if num % 10 < base:
            num = num // 10
        else:
            return False
    return True


def inputNums(k, base):
    nums = []
    i = 0
    while i < k:
        num = int(input("Input number: "))
        if isInputCorrect(num, base):
            if base == 2:
                number = TIntNumber2(num)
            elif base == 8:
                number = TIntNumber8(num)
            else:
                continue
            nums.append(number)
        else:
            print("Incorrect input!")
            i -= 1
        i += 1
    return nums

def outputNums(nums):
    for i in range (0, len(nums), 1):
        print(nums[i].getValue, end = " ")
    print()
    return

def Increment(nums):
    outputList = []
    for i in range (0, len(nums), 1):
        + nums[i]
        outputList.append(nums[i].getValue)
    return outputList

def Decrement(nums):
    outputList = []
    for i in range (0, len(nums), 1):
        - nums[i]
        outputList.append(nums[i].getValue)
    return outputList

def AllToDec(nums2, nums8):
    outputList = []
    for i in range (0, len(nums2), 1):
        outputList.append(nums2[i].convertTo10())
    for j in range (0, len(nums8), 1):
        outputList.append(nums8[j].convertTo10())
    return outputList

