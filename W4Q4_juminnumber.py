# Q4.  주민등록번호의 앞 6자리는 생년월일이고 뒷자리의 시작번호는 성별을 나타냅니다. 주민등록번호를 입력하면 몇년 몇월 생인지 그리고 남자인지 여자인지 출력하는 함수를 만들어 봅시다.

def check_id(jumin) :
    juminArr = jumin.split("-")
    afterAnswer = sex = ""

    if not len(juminArr) == 2 or not len(juminArr[0]) == 6 or not len(jumin) == 14 :
        raise

    if juminArr[1][0] in ("1","3") :
        sex = "남자"
    elif juminArr[1][0] in ("2","4") :
        sex = "여자" 
    else :
        raise

    if 0 <= int(juminArr[0][:2]) <= 21 :
        afterAnswer = input("2000년 이후 출생자 입니까? 맞으면 o 아니면 x : ")

    if afterAnswer == "o" and juminArr[1][0] not in ("3","4") :
        raise

    return juminArr[0][:2]+"년"+juminArr[0][2:4]+"월 "+sex
    
try :
    juminNum = input("주민등록번호를 입력해주세요(ex: 931204-2222222) : ")
    print(check_id(juminNum))
except :
    print("잘못된 번호입니다.\n올바른 번호를 넣어주세요")