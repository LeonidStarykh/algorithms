n = int(input())

lst = []
dct = {}

for _ in range(n):
    d, a = map(int, input().split())
    if not dct.get(d):
        dct[d] = 0
        lst.append(d)
    dct[d] += a

for val in sorted(lst):
    print(val, dct[val])