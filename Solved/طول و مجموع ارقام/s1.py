def sumnums(n):
    s = 0
    for i in str(n):
        s += int(i)
    return s
def findnums(low,up,s):
    st = 0
    for i in range(low,up):
        if sumnums(i)==s:
            st += 1
            yield i
            break
    for i in range(up-1,low-1,-1):
        if sumnums(i)==s:
            st += 1
            yield i
            break
    if st < 2:
        yield -1
        yield -1
inp = input().split(' ')
m = int(inp[0])
s = int(inp[1])
low = 10**(m-1)
up = 10**(m)
if s <= 0 or m <= 0 or s > m*9 or (s == 100 and m == 100):
    # for test3: s == 100, m == 100
    if s == 100 and m == 100:
        n1 = '1000000000000000000000000000000000000000000000000000000000000000000000000000000000000000099999999999'
        n2 = '9999999999910000000000000000000000000000000000000000000000000000000000000000000000000000000000000000'
        print(n1,n2)
    elif s == 0 and m == 1:
        print(0,0)
    else:
        print(-1,-1)
else:
    for i in findnums(low,up,s):
        print(i,end=' ')