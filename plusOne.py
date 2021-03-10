# Author: Md Tahmid Hossain
# URL: http://www.tahmidhossain.com

'''
Problem:
Given a non-empty array of decimal digits representing a non-negative integer, increment one to the integer.
The digits are stored such that the most significant digit is at the head of the list, and each element in the array contains a single digit.
You may assume the integer does not contain any leading zero, except the number 0 itself.
'''


digits = [4,3,2,1]
carry = True

for i in range(len(digits)-1, -1, -1):

    if(digits[i] == 9 and carry == True ):
        digits[i] = 0
        if(i==0):
            digits.insert(0, 1)
    elif(carry == True):
        digits[i] = digits[i]+1
        carry = False

print(digits)

