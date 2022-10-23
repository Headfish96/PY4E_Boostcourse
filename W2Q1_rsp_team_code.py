import random
dataMapping = ["가위","바위","보"]
def convertInput(inputData) :
    inputDataInt = 0;
    if inputData == "가위" :
        inputDataInt = 0;
    elif inputData == "바위" :
        inputDataInt = 1;
    elif inputData == "보" :
        inputDataInt = 2;
    else :
        try :
            inputDataInt = int(inputData)                
            if inputDataInt > 2 or inputDataInt < 0 :
                Raise
        except :
            print("입력 값이 잘못 되었습니다.")
    
    return inputDataInt
def result(my, computer) :
    print("나:",dataMapping[my])
    print("컴퓨터:",dataMapping[computer])
    if(my == computer) :
        print("동점입니다.")
    elif(computer - my in {1,-2}) :
        print("컴퓨터 승리!")
    else :
        print("나의 승리!")
        
inputData = input("가위 바위 보! :: ")
my = convertInput(inputData)
computer = random.randint(0,2);
result(my,computer)
