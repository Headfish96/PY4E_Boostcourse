import datetime

print("나이 변환 프로그램입니다. - 한국나이세어 미국나이")

while True: #올바른 값을 입력할때까지 반복한다.
    birthday = input("생년월일을 입력해주세요 / 8글자로 입력바랍니다.: ")
    birthdaylength = len(birthday)

    if birthdaylength == 8:
        byear = birthday[0:4]
        bmonth = birthday[4:6]
        bday = birthday[6:8]
        print(f'당신의 생일은 {byear}년 {bmonth}월 {bday}일 입니다.')
        break

dt_now = datetime.datetime.now()

print("현재날짜는", dt_now.year, "년", dt_now.month, "월", dt_now.day,"일 입니다.")

Kage = int(dt_now.year) - int(byear) + 1
print('당신의 한국 나이는', Kage, '입니다.')

if int(dt_now.month) > int(bmonth): #올해 생일이 지난 경우
    Aage = Kage - 1
    print('당신의 미국 나이는', Aage, '입니다.')
elif int(dt_now.month) == int(bmonth): #현재 월과 내 생일의 월이 같음. 월만보고 생일이 지났는지 안지났는지 알 수 없음
    if int(dt_now.day) >= int(bday): #올해 생일이 지났거나 오늘이 생일 당일임
        Aage = Kage - 1
        print('당신의 미국 나이는', Aage, '입니다')
    else: #올해 생일이 지나지 않았음
        Aage = Kage - 2
        print('당신의 미국 나이는', Aage, '입니다.')
else: #올해 생일이 지나지 않은 경우
    Aage = Kage - 2
    print('당신의 미국 나이는', Aage, '입니다.')
