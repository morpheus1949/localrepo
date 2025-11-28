import math


def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False

    for i in range(3, int(math.sqrt(n)), 2):
        if n % i == 0:
            return False
    return True


startnum = int(input("Enter a starting number: "))
endnum = int(input("Enter the end number: "))

while (startnum < endnum):
    if is_prime(startnum):
        print(startnum)
    startnum += 1
