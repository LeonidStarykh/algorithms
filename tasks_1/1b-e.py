d = int(input())
x, y = map(int, input().split())

if x >= 0 and y >=0 and x + y <= d:
    print(0)
else:
    dist_a = ((x - 0) ** 2 + (y - 0) ** 2) ** 0.5
    dist_b = ((x - d) ** 2 + (y - 0) ** 2) ** 0.5
    dist_c = ((x - 0) ** 2 + (y - d) ** 2) ** 0.5
    data = [(dist_a, 1),(dist_b, 2),(dist_c, 3)]
    print(min(data)[1])