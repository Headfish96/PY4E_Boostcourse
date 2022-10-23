# Q2
# 학생 답

s = ["김갑,3242524215",
"이을,3242524223",
"박병,2242554131",
"최정,4245242315",
"정무,3242524315",
"석호1,123456789",
"석호2,!234567891",
"정무2,3242524315",
"박병2,2242554131"]

# 정답지
a = [3,2,4,2,5,2,4,3,1,2]

def grader(s, a) :

    # 이름과 답을 분리하기
    name = ""
    answer = ""
    nameList = ""
    scoreList = ""
    point = 100 / len(a)

    for i in range(0, len(s)) :
        
        comma = s[i].index(",")
        name  = s[i][0:comma]
        answer = s[i][comma+1:len(s[i])]

        # 학생의 제출한 답이 이상한 경우 다시 재출하여 채점하기 위해 Error 처리
        # 마지막 등수에는 포함 안시킴
        # 학생이 제출한 정답의 개수와 정답지의 개수가 같은지 확인하기
        if len(a) != len(answer) :
            print(name, "학생 정답 수와 정답의 개수가 다릅니다!")
            continue

        # 학생이 제출한 정답이 숫자인지 확인하기
        try :
            answer = int(answer)
        except :
            print(name, "학생의 정답이 숫자가 아닙니다!")
            continue

        nameList = nameList + name + " "

        answer = str(answer)
        
        # 학생의 정답과 정답지를 비교하기

        score = 0

        for i in range(0,len(a)) :
            if answer[i] == str(a[i]) :
                score = score + point

        scoreList = scoreList + str(score) + " "

    nameList = nameList.split()
    scoreList = scoreList.split()

    pointCheck = 100
    place = 0

    while pointCheck > -1 :

        # 동점자 처리 위한 변수
        sameCheck = 0

        for i in range(0, len(scoreList)) :

            if str(pointCheck) == str(scoreList[i]) :

                print("학생 :", nameList[i], "점수 :", scoreList[i], "등수 :", place+1, "등")
                sameCheck = sameCheck + 1
        
        pointCheck = pointCheck - point
        place = place + sameCheck

grader(s, a)