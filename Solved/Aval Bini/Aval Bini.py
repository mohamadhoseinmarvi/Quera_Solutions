# اول بینی
# ID : 649
# https://quera.ir/problemset/university/649/%D8%B3%D8%A4%D8%A7%D9%84-%D8%AF%D8%A7%D9%86%D8%B4%DA%AF%D8%A7%D9%87-%D8%B5%D9%86%D8%B9%D8%AA%DB%8C-%D8%B4%D8%B1%DB%8C%D9%81-%D9%85%D8%A8%D8%A7%D9%86%DB%8C-%D8%A8%D8%B1%D9%86%D8%A7%D9%85%D9%87%D9%86%D9%88%DB%8C%D8%B3%DB%8C-%D9%BE%D8%A7%DB%8C%DB%8C%D8%B2-%DB%B9%DB%B3-%D8%A7%D9%88%D9%84%D8%A8%DB%8C%D9%86%DB%8C
# https://b2n.ir/f91551

a, b = int(input()), int(input())

result = ""
for i in range(a + 1, b):
    count = 0
    for j in range(1, i + 1):
        if i % j == 0:
            count += 1

    if count == 2 and not result:
        result = str(i)
    elif count == 2:
        result += "," + str(i)

print(result)

###########################################################

s, e = int(input()), int(input())

lst = []

for x in range(s + 1, e):
    flag = False
    for y in range(2, x // 2 + 1):
        if x % y == 0:
            flag = True
            break
    if flag == False:
        lst.append(x)

print(*lst, sep=",")


###########################################################

def isPrime(number):
    for j in range(2, number):
        if number % j == 0:
            return False
    return True


a, b = int(input()), int(input())

result = []

for number in range(a + 1, b):
    count = 0

    if isPrime(number):
        result.append(str(number))

print(",".join(result))
