x, y, z = map(int, input().split())

if (1 <= x <= 12) and (1 <= y <= 12) and (x != y):
    print(0)
else:
    print(1)