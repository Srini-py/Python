'''
Create an algorithm to turn an ordinary fraction a / b, 
where a < b, into an Egyptian fraction.
'''


from math import ceil

def egyptian_fraction(num, denom):
  return ceil(denom/num)


num, denom = map(int, input("Enter the numerator and denominator to find egyptian fraction : ").split())

while num != 0:
    denom1 = egyptian_fraction(num, denom)
    num = denom1*num - denom
    denom = denom*denom1
    print("1/{}".format(denom1), end = " + ")