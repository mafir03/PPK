n = ord(input().upper())
a = 65

lists = []
# buat template segitiga A-Z
for _ in range(1,8):
    temp = []
    for __ in range(a, a + _):
        # perbaris
        if a > 90:
            break
        a += 1
        temp.append(chr(__))
    lists.append(temp)

for _ in range(len(lists)):
    for __ in range(len(lists[_])):
        # jika huruf di lists[_][__] < huruf input
        if ord(lists[_][__]) < n:
            lists[_][__] = chr(n)

for item in lists:
    print(" ".join(item))
        
