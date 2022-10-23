# Q4
### 새로운 달의 마지막 날이 100일 기념일을 지나치는지 확인하여 계산합니다.

def after_100(mm,dd,day):
    d = [31,28,31,30,31,30,31,31,30,31,30,31]
    week =["월","화","수","목","금","토","일"]
    
    if day == "일": the_day = "월"
    else : the_day = week[week.index(day)+1]
    
    month_index = mm-1
    count = d[month_index] - dd + 1
    
    try:
        if type(mm) == int and  0 < mm < 13 and type(dd) ==int and 0 < dd <= d[month_index] and day in week:
            for i in range(4):
                month_index += 1
                if month_index > 11:
                    month_index -= 12
                count = count + d[month_index]
                if count < 100:
                    continue
                elif count == 100:
                    d_month = month_index + 1
                    d_day = d[month_index] 
                    break
                elif count > 100:
                    d_month = month_index + 1
                    d_day = d[month_index] - (count-100)
                    break
            
            print(str(mm)+"월 "+str(dd)+"일 "+day+"요일부터 100일 뒤는 "+str(d_month)+"월 "+str(d_day)+"일 "+the_day+"요일")
        else: raise
    except:
        print("인수 오류")
        
after_100(6,21,"화")