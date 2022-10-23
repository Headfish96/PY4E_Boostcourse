def takemoney():
    while True:
        try:
            money = int(input("금액을 입력해주세요:"))
            if money > 0:
                print("당신이 입력한 숫자는 양의 정수입니다.")
                break
            else:
                print("양의 정수를 입력해주세요")
        except ValueError:
            print("숫자를 입력해주세요")
    return money

def money_with_comma():
    money = takemoney()
    money_str = str(money)
    if len(money_str)%3 == 0:
        for i in range(0, len(money_str)//3 -1):
            money_str = money_str[:-(4*i + 3)] + ',' + money_str[-(4*i + 3):]
    elif len(money_str)%3 != 0:
        for i in range(0, len(money_str)//3):
            money_str = money_str[:-(4 * i + 3)] + ',' + money_str[-(4 * i + 3):]

    return money_str
    
print(money_with_comma())