import string
import random


def randompassword():
    chars=string.ascii_uppercase + string.ascii_lowercase + string.digits
    size = 1
    return ''.join(random.choice(chars) for x in range(size,10))

n = 0
while n < 5:
    print(randompassword())
    n=n+1
