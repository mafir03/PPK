n = int(input())

def checkIfPrime(n):
    for _ in range(2, n):
        if _ == 1:
            continue
        else:
            if n % _ == 0:
                return False
    return True


for _ in range(1, n + 1):
    if checkIfPrime(_) == False:
        continue
    else:
        if _ == 1:
            continue
        else:
            print(_, end=" ")