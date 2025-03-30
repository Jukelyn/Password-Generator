"""
Random Password generator
"""
import random
import string

MAX_LENGTH: int = 32

# Prefer more letters than digits and more digits than punctuation
LEGAL_SET = string.ascii_letters * 2 + string.punctuation + \
    string.digits * 2  # Long string of a-Z, 0-9, and punctuation with bias

try:
    req_len = int(input("How long do you want your password to be? "))
except ValueError:
    req_len: int = MAX_LENGTH


def randomizer(length: int = MAX_LENGTH) -> str:
    """
    Generates a randomized password using the characters in legal_set

    Args:
        length (int): The length of the password.

    Returns:
        (str): The password.
    """
    if length > MAX_LENGTH:
        msg = f'The maximum length for a password is {MAX_LENGTH} characters.'
        raise ValueError(msg)

    result = ''
    for _ in range(0, length):
        letter = random.choice(LEGAL_SET)
        result += letter
    return result


output = randomizer(req_len)
print(f'Your randomly generated password of length {len(output)} is {output}')
