a, k, b, m, x = map(int, input().split())

l = 0
r = 2 * x

while l < r:
    days = (l + r) // 2
    hd = days // k
    hf = days // m
    tree_felling = (days - hd) * a + (days - hf) * b
    if tree_felling < x:
        l = days + 1
    else:
        r = days

print(l)