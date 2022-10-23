def after_tax(before_tax):
    if before_tax < 0:
        raise
    elif before_tax <= 1200:
        r= 0.06
    elif before_tax <= 4600:
        r = 0.15
    elif before_tax <= 8800:
        r = 0.24    
    elif before_tax <= 15000:
        r = 0.35
    elif before_tax <= 30000:
        r = 0.38
    elif before_tax <= 50000:
        r = 0.40
    else:
        r = 0.42
    return(int(before_tax*(1-r)))
try :
    monthly_payment = int(input("월급을만원단위로입력해주세요 : "))
    before_tax = 12*monthly_payment
    after_tax = after_tax(before_tax)
    print("세전연봉: ",before_tax,"만원")
    print("세후연봉: ",after_tax, "만원")    
except :
    print("입력값이 잘못되었습니다.")
    quit()