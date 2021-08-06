'''
Given a sorted array, 
find the smallest positive integer that is not the sum of a subset of the array.
'''

length = int(input("Enter the length of the array :"))
arr = list(map(int,input("Enter the elements in the array, space seperated :").split()))

result = 1
for num in arr:
    if num <= result:
        result += num
    else:
        break
        
print(result)