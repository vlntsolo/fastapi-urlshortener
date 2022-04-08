import string
import random




def generate_slug():
    # printing letters
    letters = string.ascii_letters
    return ''.join(random.choice(letters) for i in range(10))