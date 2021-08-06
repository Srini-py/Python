# Given a array of numbers representing the stock prices of a company in chronological order, 
# write a function that calculates the maximum profit you could have made from buying and selling that stock once. 
# You must buy before you can sell it.

# For example, given [9, 11, 8, 5, 7, 10], you should return 5, 
# since you could buy the stock at 5 dollars and sell it at 10 dollars.

def findMaxProfit(a, n):
    max_diff = a[1] - a[0]
    min_el = a[0]
    for i in range(1, n):
        if a[i] - min_el > max_diff:
            max_diff = a[i] - min_el
        
        if a[i] < min_el:
            min_el = a[i]
    return max_diff, min_el



prices = [int(i) for i in input('Enter the stock prices in space seperated integers: ').split()]
times = len(prices)

diff, start = findMaxProfit(prices, times)
print(f'Maximum profit {diff} is obtained when bought at {start} and sold at {start + diff}')