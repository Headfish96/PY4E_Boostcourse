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

money = takemoney()
money_with_comma = format(money, ',')
print(money_with_comma)