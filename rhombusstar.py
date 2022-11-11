n = int(input())
# (n + (n - 1)) = panjang string pada string terpanjang
for _ in range(1, n+1):
    print(("* " * _).center(n + (n - 1)))

for __ in range(n - 1, 0, -1):
    print(("* " * __).center(n + (n - 1)))