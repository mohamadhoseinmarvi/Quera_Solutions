# بازی
# ID : 52543
# https://quera.org/problemset/52543/
# https://b2n.ir/m62054

a = int(input())
b = list(map(int, input().split()))
m = ""

for i in range(a):
    if len(b) >= 2:
        m += str(max(b)) + " "
        m += str(min(b)) + " "
        b.remove(max(b))
        b.remove(min(b))

    elif len(b) == 1:
        m += str(b[0]) + " "
        break

print(m)
