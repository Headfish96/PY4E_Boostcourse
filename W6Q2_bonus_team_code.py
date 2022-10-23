# 이름, 실적
member_names = ["갑돌이", "갑순이", "을돌이", "을순이", "병돌이", "병순이", "석호"]
member_records = [[4,5,3,5,6,5,3,4,1,3,4,5],[2,3,4,3,1,2,0,3,2,5,7,2], 
           [1,3,0,3,3,4,5,6,7,2,2,1],[3,2,9,2,3,5,6,6,4,6,9,9],
           [8,7,7,5,6,7,5,8,8,6,10,9],[7,8,4,9,5,10,3,3,2,2,1,3], [10, 10, 10]]

def recordsAvg(records) :

    avg = list()

    # 실적 길이에 유동적이게 len 함수 활용
    for i in range(0, len(records)) :
        sum = 0
        recordsList = records[i]
        for j in range(0, len(recordsList)) :
            sum = sum + recordsList[j]

        # 실적 평균을 따로 저장
        avg.append(sum/len(recordsList))

    return avg

def bonus(name, avg) :

    # 입력 값 개수가 잘못된 경우
    if len(name) != len(avg) :
        print("입력값 개수가 잘못 되었습니다!")
    
    else :
        # 정렬된 리스트로 최대/최소와 두번째 큰/작은 값 구하기
        sortedAvg = sorted(avg)
        firstMax  = sortedAvg[-1]
        secondMax = sortedAvg[-2]
        firstMin  = sortedAvg[0]
        secondMin = sortedAvg[1]

        print("======== 보너스 대상자 ========")

        # 보너스 대상자 2명
        if secondMax > 5 :

            firstBonus = name[avg.index(firstMax)]
            secondBonus = name[avg.index(secondMax)]
            print("보너스 대상자 :", firstBonus)
            print("보너스 대상자 :", secondBonus)

        # 보너스 대상자 1명
        elif firstMax > 5 :
            firstBonus = name[avg.index(firstMax)]
            print("보너스 대상자 :", firstBonus)

        else :
            print("보너스 대상자가 없습니다!")

        print("")
        print("======== 면담   대상자 ========")

        # 면담 대상자 2명
        if secondMin < 3 :

            firstMeet = name[avg.index(firstMin)]
            secondMeet = name[avg.index(secondMin)]
            print("면담 대상자 :", secondMeet)
            print("면담 대상자 :", firstMeet)

        # 면담 대상자 1명
        elif firstMin < 3 :
            firstMeet = name[avg.index(firstMin)]
            print("면담 대상자 :", firstMeet)

        else :
            print("면담 대상자가 없습니다!")

recordsAvg(member_records)
bonus(member_names, recordsAvg(member_records))