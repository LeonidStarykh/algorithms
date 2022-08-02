arr = list(map(int, input().split()))
eps = 1e-6

def func(x):
    return arr[0]*x*x*x + arr[1]*x*x + arr[2]*x + arr[3]

r = 1
while func(r) * func(-r) >= 0:
    r *= 2
l = -r

while r - l > eps:
    m = (l + r) / 2
    if func(m) * func(r) > 0:
        r = m
    else:
        l = m

print((l+r)/2)
