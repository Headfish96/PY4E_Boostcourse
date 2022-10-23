def cal_garde(score):
    if 95 <= score:
        grade = "A+"
    elif 90 <= score:
        grade = "A"
    elif 85 <= score:
        grade = "B+"
    elif 80 <= score:
        grade = "B"
    elif 75 <= score:
        grade = "C+"
    elif 70 <= score:
        grade = "C"
    elif 65 <= score:
        grade = "D+"
    elif 60 <= score:
        grade = "D"
    else:
        grade = "F"
    return grade

try:
    #자료형을 숫자로 변환
    name = str(input("이름을 입력하세요"))
    score = int(input("성적을 입력해주세요요"))
    print("성명:", name)
    print("점수:", score)
    print("성적:", cal_garde(score))
except ValueError as exception:
    print("이름은 한글 성적은 숫자로 입력바랍니다.")