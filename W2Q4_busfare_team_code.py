def busfare_cash(age):
    if 8 <= age < 14:
        fare = 450
    elif 14 <= age < 20:
        fare = 1000
    elif 20 <= age < 75:
        fare = 1300
    else:
        fare = 0
    return fare
def busfare_card(age):
    if 8 <= age < 14:
        fare = 450
    elif 14 <= age < 20:
        fare = 720
    elif 20 <= age < 75:
        fare = 1200
    else:
        fare = 0
    return fare
#자료형을 숫자로 변환
try:
    age = int(input("나이를 입력해주세요: "))
    if age <= 0:
        raise Exception
except:
    print("입력가능한 수치를 초과하였습니다.")
else:
    try:
        type = input("지불 유형을 입력해주세요(현금/카드): ")
        if type == "현금":
            print("버스요금:",busfare_cash(age))
        elif type == "카드":
            print("버스요금:",busfare_card(age))
        else:
            print("현금 또는 카드만 가능합니다.")
    except ValueError as exception:
        print("나이는 숫자로, 지불 유형은 한글로 입력 바랍니다.")