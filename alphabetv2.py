n = int(input())
a = 65
for _ in range(1, n+1):
    print(chr(a) * _)
    if a > 90:
        break
    a += 1
