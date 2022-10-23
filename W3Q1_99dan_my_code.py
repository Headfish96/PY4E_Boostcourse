def gugudan(number):
    for i in range(1, 10):
        if i % 2 == 1:
            result = number * i
            if result <= 50:
                print(f'{number} X {i} = {result}')

def check_input():
    while True:
        try:
            number = int(input("구구간 몇단? / 숫자를 입력해주세요"))
            if(number > 0):
                print("당신이 입력한 숫자는 양의 정수 입니다.", number)
                break
            elif(number > 10):
                print("입력값 오류입니다. 1~9까지의 숫자를 입력해주세요")
            else:
                print("입력값 오류입니다. 양의 정수를 입력해주세요.")
        except ValueError:
            print("입력값 오류입니다. 숫자를 입력해주세요")
    return number
    
gugudan(check_input())