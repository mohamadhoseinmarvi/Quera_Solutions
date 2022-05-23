import math as m
def calc(a,b,c):
    if a == 0:
        x = (-c)/b
        return x
    elif b == 0:
        x = abs(m.sqrt((-c)/a))
        if not x == 0:
            return -x,x
        else:
            return x
    elif (b**2) < (4*a*c):
        return None
    else:
        sq = m.sqrt(abs((b**2)-(4*a*c)))
        x1 = (-b + sq)/(2*a)
        x2 = (-b - sq)/(2*a)
        if x1 > x2:
            return x2,x1
        elif x2 > x1:
            return x1,x2
        else:
            return x1
    return None
def printans(a,b,c):
    x = []
    x = calc(a,b,c)
    if x == None:
        print('IMPOSSIBLE')
    else:
        try:
            for i in x:
                try:
                    print('%.3f'%i)
                except :
                    print(i)
        except :
            print('%.3f'%x)
a = float(input())
b = float(input())
c = float(input())
if a == b == 0 or a > 100 or b > 100 or c > 100 or a < -100 or b < -100 or c < -100:
    print("IMPOSSIBLE")
else:
    printans(a,b,c)