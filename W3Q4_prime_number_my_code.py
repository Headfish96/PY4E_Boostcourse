a = int(input("첫 번째 숫자를 입력하세요"))
b = int(input("두 번째 숫자를 입력하세요"))
d = 0

for i in range(a, b+1):
    c = 0
    for j in range(2, i):
        if i % j == 0:
            c = 1

    if c == 0:
        d = d + 1
        print("{}는 소수입니다.".format(i))
    else:
        print("{}는 소수가 아닙니다.".format(i))
print("소수의 개수는 {}입니다.".format(d))