# Q1. 숫자를 입력 받고 그 숫자의 구구단을 출력하는 함수를 만들어 봅시다. 다만 아래의 조건을 만족해 주세요.

def gugudan(number):
    for i in range(1, 10):
        if i % 2 == 1:
            result = number * i
            if result <= 50:
                print(f'{number} X {i} = {result}')
try:
    number = int(input("몇 단? : "))
    gugudan(number)
    
except:
    print('숫자만 입력해주세요!!')
