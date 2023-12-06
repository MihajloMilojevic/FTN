import random
import string


def generate_string(len: int, lower=True, upper=True, digits=True):
    chars = ""
    if lower:
        chars += string.ascii_lowercase
    if upper:
        chars += string.ascii_uppercase
    if digits:
        chars += string.digits
    if chars == "":
        return ""
    return ''.join([random.choice(chars) for _ in range(len)])


def generate_number(min, max):
    return random.randint(min, max)
