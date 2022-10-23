def take_monthly_pay():
        yearpay_bf_tax = monthly_pay * 6
        if yearpay_bf_tax <= 1200:
            yearpay_af_tax = yearpay_bf_tax * 0.96
        elif 1200 < yearpay_bf_tax <= 4600:
            yearpay_af_tax = yearpay_bf_tax * 0.85
        elif 4600 < yearpay_bf_tax <= 8800:
            yearpay_af_tax = yearpay_bf_tax * 0.76
        elif 8800 < yearpay_bf_tax <= 15000:
            yearpay_af_tax = yearpay_bf_tax * 0.65
        elif 15000 < yearpay_bf_tax <= 30000:
            yearpay_af_tax = yearpay_bf_tax * 0.62
        elif 30000 < yearpay_bf_tax <= 50000:
            yearpay_af_tax = yearpay_bf_tax * 0.60
        else:
            yearpay_af_tax = yearpay_bf_tax * 0.58
        print("세전 연봉:", yearpay_bf_tax)
        print("세후 현봉:", yearpay_af_tax)
def check_monthly_pay():
    try:
        monthly_payment = int(monthly_pay)
    except ValueError as exception:
        print("월급은 숫자로 입력해주시기 바랍니다.")
    except IndexError as exception:
        print("입력가능한 수치를 초과하였습니다.")
monthly_pay = int(input("월급을 입력해주세요:"))
take_monthly_pay()
check_monthly_pay()