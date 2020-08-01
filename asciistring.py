#ascii string
for _ in range(int(input())):
    s = input()
    count = 0
    for i in s:
        c = abs(96-ord(i))
        if c==s.count(i):
            count = count + 1
        else:
            break
    if count==len(s):
        print("YES",end=" ")
    else:
        print("NO",end=" ")
print()
    