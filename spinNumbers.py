n = int(input())

for _ in range(1, n):
    if _ == 1:
        for __ in range(1, n):
            if __ == n - 1:
                print(__)
            else:
                print(__, end="", sep="")
    else:
        lists = []
        for ___ in range((n - (n - _)), n):
            lists.append(str(___))
        for dot in range(1, (n - (n - _))):
            lists.append(str(dot))
        print("".join(lists))