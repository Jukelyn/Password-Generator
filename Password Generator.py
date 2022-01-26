# Random Password generator
# Input: Length
# Output: str of length Length

import random
import string

req_len = int(input("How long do you want your password to be? "))
legal_set = string.ascii_letters * 3 + string.punctuation + string.digits * 2 # Long string of a-Z, 0-9, and punctuation with bias

# Prefer more letters than digits and more digits than punctuation

def randomizer(Length: int) -> str: # Generates a randomized password using the characters in legal_set
    if Length > 32:
        print('The maximum length for a password is 32 characters.')
    else:
        if Length > 16: # 16 chars is the max for a lot of sites
            print('The length is greater than 16 chracters.')   
        result = ''
        for i in range(1, Length + 1):
            letter = random.choice(legal_set)
            result += letter
        return result # returns a str that has a length of Length

try:
    output = randomizer(Length=req_len)
    password = ''.join(random.sample(output,len(output))) # Randomize again bc why not lol
    pass_len = len(password)
    print(f'Your randomly generated password of length {pass_len} is {password}')
except (NameError, TypeError): # Should really only be using this if Length > 32
    pass
