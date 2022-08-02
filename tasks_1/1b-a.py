zad = int(input())
inter = int(input())
check = int(input())

if inter == 0:
    if zad == 0:
        print(check)
    else:
        print(3)
elif inter == 4:
    if zad == 0:
        print(4)
    else:
        print(3)
elif inter == 1:
    print(check)
elif inter == 6:
    print(0)
elif inter == 7:
    print(1)
else:
    print(inter)
