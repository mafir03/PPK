x, y = map(int, input().split())
xx,yy = map(int, input().split())
maps = []

# bikin map
for _ in range(y):
    temp = ['*' for __ in range(x)]
    maps.append(temp)

# cetak posisi pergerakan
if xx == 0 and yy == 0:
    maps[0][0] = '0'
else:
    maps[0][0] = '0'
    for _ in range(1, len(maps)):
        try:
            maps[yy * _][xx * _] = f'{_}'
        except IndexError: # pergerakan lebih dari ukuran map
            break

# print hasil
for item in maps:
    temps = []
    for letter in item:
        temps.append(letter)
    print("".join(temps))
    