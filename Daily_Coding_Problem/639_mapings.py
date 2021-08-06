'''
Given a mapping of digits to letters (as in a phone number), 
and a digit string, return all possible letters the number could represent. 
You can assume each valid number in the mapping is a single digit.

For example if {“2”: [“a”, “b”, “c”], 3: [“d”, “e”, “f”], …} then “23” should return 
[“ad”, “ae”, “af”, “bd”, “be”, “bf”, “cd”, “ce”, “cf"].
'''

from itertools import product

mapped_dictionary = {
                     1: ['.', ',', '!'], 2: ['a', 'b', 'c'], 3: ['d', 'e', 'f'], 
                     4: ['g', 'h', 'i'], 5: ['j', 'k', 'l'], 6: ['m', 'n', 'o'], 
                     7: ['p', 'q', 'r', 's'], 8: ['t', 'u', 'v'], 9: ['w', 'x', 'y', 'z']
                    }
                    
digit_string = input()

print([''.join(mapped) for mapped in list(product(*[mapped_dictionary[int(i)] for i in digit_string]))])