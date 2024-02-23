import string
import random

while True:
    x1 = string.ascii_uppercase
    x2 = string.ascii_lowercase
    x3 = string.digits
    x4 = string.punctuation
    plen = int(input("Enter password length: "))
    x = []
    x.extend(list(x1))
    x.extend(list(x2))
    x.extend(list(x3))
    x.extend(list(x4))
    random.shuffle(x)
    print("Generated Password:", "".join(x[0:plen]))

    choice = input("Do you want to generate another password? (yes/no): ")
    if choice.lower() != 'yes':
        breakpoint