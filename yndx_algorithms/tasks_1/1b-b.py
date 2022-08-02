N, i, j = map(int,input().split())
if i < j:
    if j-i > N/2:
        print(abs(j-i-N)-1)
    else:
        print(j-i-1)
else:
    if i-j > N/2:
        print(abs(i-j-N)-1)
    else:
        print(i-j-1)