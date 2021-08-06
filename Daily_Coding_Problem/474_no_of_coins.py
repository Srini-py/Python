'''
Find the minimum number of coins required to make n cents.
You can use standard American denominations, that is, 1¢, 5¢, 10¢, and 25¢.
For example, given n = 16, return 3 since we can make it with a 10¢, a 5¢, and a 1¢.
'''


n = int(input("Enter no.of cents : "))

no_of_25 = n // 25
n -= 25 * no_of_25
no_of_10 = n // 10
n -= 10 * no_of_10
no_of_5 = n // 5
n -= 5 * no_of_5
no_of_1 = n // 1

print("Minimum no.of coins required are", no_of_25 + no_of_10 + no_of_5 + no_of_1)