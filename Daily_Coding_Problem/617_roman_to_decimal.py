'''
Given a number in Roman numeral format, convert it to decimal.
'''

roman = {
    'M': 1000,
    'D': 500,
    'C': 100,
    'L': 50,
    'X': 10,
    'V': 5,
    'I': 1
}

roman_number = input("Enter a valid roman number : ")
max = 0
total = 0
for char in roman_number[-1::-1]:
  if roman[char] >= max:
    total += roman[char]
    max = roman[char]
  else:
    total -= roman[char]

print(total)