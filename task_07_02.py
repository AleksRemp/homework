import random
from string import digits, ascii_letters


def password_generator(n):
    listing = list(digits + ascii_letters)
    for i in range(n):
        letter = random.choice(listing)
        yield letter