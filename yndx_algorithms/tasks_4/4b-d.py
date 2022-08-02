part = []
dct = {}
with open('duma.txt', 'r') as text:
    summ = 0                            # общее количество проголосовавших
    for line in text:
        arr = line.split()
        name = ' '.join(arr[:-1])       # название партии
        val = int(arr[-1])              # количество голосов за партию
        summ += val
        part.append([name, val])
        dct[name] = val

first_ratio = summ / 450.
summ = 0
# arr = []
for k in range(len(part)):
    part[k].append(int(part[k][1] // first_ratio))
    part[k].append((part[k][1] / first_ratio) % 1)
    # arr.append([k, dct[k][2], dct[k][0]])
    summ += part[k][2]

if summ < 450:
    part = sorted(part, key=lambda x: (x[3],x[1]), reverse=True)
    for i in range(450-summ):
        part[i][3] += 1

for i in range(len(part)):
    dct[part[i][0]] = part[i][2] + (part[i][3] // 1)

for k in dct:
    print(k, int(dct[k]))

# print(dct)
# print(part)


