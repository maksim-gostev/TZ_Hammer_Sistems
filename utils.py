import random
import string

def generate_random_string():
    letters_and_numbers = string.ascii_letters + string.digits
    return ''.join(random.sample(letters_and_numbers, 6))


def generate_random_digits():
    digits = string.digits
    return ''.join(random.sample(digits, 4))

