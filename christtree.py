n = int(input())

for _ in range(1, n + 2):
    if _ == 1:
        print('|'.center(n*2 + 1))
    else:
        print(('*' * (_ - 1) + '|' + '*' * (_ - 1)).center(n*2 + 1))