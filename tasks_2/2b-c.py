data = list(map(str, input()))

cnt = 0
for i in range(len(data)):
    if data[i] != data[-i - 1]:
        cnt += 1
print(cnt//2)