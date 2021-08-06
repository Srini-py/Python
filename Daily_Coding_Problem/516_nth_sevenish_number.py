'''
Create an algorithm to find the nth sevenish number.
'''


n = int(input("Enter the value of n : "))
binary_n = bin(n)[2:]
nth_sevenish = int(binary_n, base = 7)
print(nth_sevenish)