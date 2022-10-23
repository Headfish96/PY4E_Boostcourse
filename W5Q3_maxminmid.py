# Q3

import random

gNumbers = None
def makeNumbers() :
    numbers = list()
    while(len(numbers) < 3) :
        number = random.randint(0, 100)
        if number in numbers : continue
        numbers.append(number)

    numbers.sort()
    return numbers

def guessCheck(number,guessCount) :
        min = gNumbers[0] - number
        mid = gNumbers[1] - number
        max = gNumbers[2] - number

        rangeComment = ["최솟값","중간값","최댓값"]
        if abs(mid) > abs(min) < abs(max)  : valueList = [0,min]
        elif abs(min) > abs(mid) < abs(max)  : valueList = [1,mid]
        else : valueList = [2,max]

        if valueList[1] == 0 : 
            print("숫자를 맞추셨습니다.!",str(number)+"는",rangeComment[valueList[0]] + "입니다")
            return 1
        elif valueList[1] != 0 and guessCount in (5,10) :
            print(rangeComment[valueList[0]]+"은",str(number),"작습니다" if valueList[1] < 0 else "큽니다.")       
            return 0     
        else :
            print(str(number)+"는 없습니다.")            
            return 0

def guessNumbers() :
    okCount = 0
    guessCount = 1
    guessHistory = list()
    while(True) :
        print(guessCount,"차 시도")

        number = input("숫자를 예측해보세요(종료 : quit) :")
        if number == "quit" : break

        try :
            number = int(number)
            if number in guessHistory : 
                print("이미 예측에 사용한 숫자입니다")
                continue

            okCount += guessCheck(number,guessCount)
            if okCount == 3 :
                print("게임종료")
                print(guessCount,"번 시도만에 예측 성공")
                return

            guessHistory.append(number)
            guessCount+=1
        except :
            print("입력값이 잘못 되었습니다.")
            continue

    print("게임종료")
    
gNumbers = makeNumbers()
print("3개의 랜덤값:",gNumbers)
guessNumbers()
