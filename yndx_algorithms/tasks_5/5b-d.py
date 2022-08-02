def isvalid():
    s = list(map(str, input()))

    if len(s) < 2:
        return False

    list1 = []

    for char in s:
        if char == '(':
            list1.append(char)
        elif not list1:
            return False
        else:
            last = list1.pop()
            if char == ')' and last != '(':
                return False
    return len(list1) == 0

ans = isvalid()
if ans == True:
    print('YES')
else:
    print('NO')
