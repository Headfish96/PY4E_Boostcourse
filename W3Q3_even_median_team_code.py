# Q3. 2개의 숫자를 입력하여 그 사이에 짝수만 출력하는 함수를 만들어 봅시다. 그리고 중앙값도 함께 출력 해봅시다.(단, 중앙값이 짝수가 아닐 경우에는 중앙값은 출력을 하지 않고, 짝수인 수만 출력한다)

def inter(a,b):
    if a<b :
        for i in range(a+1,b,1) :           
            if i%2 == 0 :
                print(i,"짝수")
                if i == (a+b)/2 :
                    print(i, "중앙값")
    elif a>b:
        for i in range(a-1,b,-1) :
            if i%2 == 0 :
                print(i,"짝수")
                if i == (a+b)/2 :
                    print(i, "중앙값")
    elif a == b:
        print("서로다른두정수를입력하세요.")
        
try:
    a = int(input("첫번째정수입력 : "))
    b = int(input("두번째정수입력 : "))
    inter(a,b)
except:
    print("정수를입력해주세요.")