'''
Implement run-length encoding and decoding. 
You can assume the string to be encoded have no digits and consists solely of 
alphabetic characters. You can assume the string to be decoded is valid.
'''


def encode(s, n):
  char_count = 0
  encoded_string = ''
  for i in range(n-1):
    char_count += 1
    if i != n - 2:
      if s[i] != s[i+1]:
        encoded_string += str(char_count) + s[i]
        char_count = 0
    else:
      if s[i] != s[i+1]:
        encoded_string += str(char_count) + s[i] + '1' + s[i+1]
      else:
        encoded_string += str(char_count + 1) + s[i+1]

  print("Encoded_string is "+encoded_string)
  return encoded_string


def decode(s, n):
  decoded_string = ''
  for i in range(0,n,2):
    decoded_string += s[i+1]*int(s[i])
  print("Decoded string is "+decoded_string)


string = input("Enter the string to run length encoding : ")
string = encode(string, len(string))
decode(string, len(string))