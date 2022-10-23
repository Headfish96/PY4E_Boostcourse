def nameinput():    # 이름에 숫자나 공백이 있을 경우 재입력을 요구함.
    name = input('이름을 입력해주세요: ')
    if name.isnumeric() or not name.isalpha() :
        print('-----------------------------')
        print('이름 입력 형식에 맞지 않습니다.')
        print('다시 입력해주세요.')
        name = nameinput()
    return name
def gradefnc(score):
    if score > 100 or score < 0  :
        raise
    elif 100 >= score >= 95:
        grade ='A+'
    elif score >= 90:
        grade ='A'
    elif score >= 85:
        grade ='B+'
    elif score >= 80:
        grade ='B'
    elif score >= 75:
        grade ='C+'
    elif score >= 70:
        grade ='C'
    elif score >= 65:
        grade ='D+'
    elif score >= 60:
        grade ='D'
    else:
        grade ='F'
    return grade
try :
    fname = nameinput()
    fscore = float(input('점수를 입력해주세요: '))    
    fgrade = gradefnc(fscore)
    print('이름 : ', fname)
    print('점수 : ', fscore)
    print('학점 : ', fgrade)
except :
    print("입력하신 점수가 잘못되었습니다.")
