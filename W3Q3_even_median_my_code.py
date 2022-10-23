def inter(startnum, endnum):
    if startnum < endnum:
        for i in range(startnum + 1, endnum, 1): #startnum+1부터 endnum가지 1의 차이씩
            if i % 2 == 0:
                print(i, "짝수")
                if i == (a + b) / 2:
                    print(i, "중앙값")
    elif startnum > endnum:
        for i in range(a - 1, b, -1):
            if i % 2 == 0:
                print(i, "짝수")
                if i == (a + b) / 2:
                    print(i, "중앙값")
                    
def check_input():
    while True:
        try:
            Start_number = int(input("첫번째 정수 입력:"))
            End_number = int(input("두번째 정수 입력:"))
            if Start_number and End_number > 0:
                break
            elif Start_number or End_numner < 0:
                print("입력값 오류입니다. 양의 정수를 입력해주세요.")
            elif Start_number == End_number:
                print("입력값 오류입니다. 서로 다른 두 정수를 입력해주세요.")
        except ValueError:
            print("입력값 오류입니다. 숫자를 입력해주세요")
    return Start_number, End_number

a, b = check_input()
inter(a, b)