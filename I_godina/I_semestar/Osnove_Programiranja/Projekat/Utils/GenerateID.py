import random
import string
 
def generateString(len: int, lower=True, upper=True, digits=True):
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

def generateNumber(min, max):
    return random.randint(min, max)