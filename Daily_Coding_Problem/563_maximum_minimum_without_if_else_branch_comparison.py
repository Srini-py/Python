'''
Find the maximum of two numbers without using any if-else statements, branching, or direct comparisons.
'''


a, b = map(int, input("Enter two distinct positive numbers : ").split())

maximum = a * bool(a//b) + b * bool(b//a)
minimum = a * bool(b//a) + b * bool(a//b)
print("Maximum number is {0} and minimum number is {1}".format(maximum, minimum))