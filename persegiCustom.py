n = int(input())

# lupa ini modul nested loop, maaf 3 soal pertama engga pake

for _ in range(n):
    if _ == 0 or _ == n - 1:
        for __ in range(n):
            if __ == 0:
                print("+", sep="", end="")
            elif __ == n - 1:
                print("+")
            else:
                print("-", sep="", end="")
    else:
        for __ in range(n):
            if __ == 0:
                print("|", sep="", end="")
            elif __ == n - 1:
                print("|")
            else:
                print("-", sep="", end="")
