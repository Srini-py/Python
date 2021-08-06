# There exists a staircase with N steps, 
# and you can climb up either 1 or 2 steps at a time. 
# Given N, write a function that returns the number of unique ways you can climb the staircase. 
# The order of the steps matters.


#To find Nth fibonacci number, formula is F(n) = [Phi^n - phi^n]/sqrt(5)
#Phi = (1 + sqrt(5))/2
#phi = (1 - sqrt(5))/2

def variableFibonacci(n, m):
    res = [0] * (n + 1)
    res[0] = 0
    res[1] = 1
    for i in range(2, n + 1):
        j = 1
        while j <= m and j <= i:
            res[i] += res[i - j]
            j += 1
    return res[n]


def count_ways(n, m):
    return variableFibonacci(n + 1, m)


def count_ways_2(n, m):
    temp = 0
    res = [1]
    for i in range(1, n + 1):
        s = i - m - 1
        e = i - 1
        if s >= 0:
            temp -= res[s]
        temp += res[e]
        res.append(temp)
    return res[n]


def count_2_ways(n):
    var1 = 0
    if n == 0:
        return var1
    var2 = 1
    if n == 1:
        return var2
    for i in range(2, n + 2):
        var1, var2 = var2, var1 + var2
    return var2


n = int(input("Enter no.of steps :"))
#m = int(input("Enter no.of steps at a time upto :"))
print(count_2_ways(n))
#print(count_ways(n, m))
#print(count_ways_2(n, m))
