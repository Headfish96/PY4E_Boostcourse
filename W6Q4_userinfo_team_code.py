# 6명의 회원이고 "아이디,나이,전화번호,성별,지역,구매횟수" 순서로 입력되어 있음
CONST_KEYS = ["아이디","나이","전화번호","성별","지역","구매횟수"]
info = "abc,21세,010-1234-5678,남자,서울,5,cdb,25세,x,남자,서울,4,bbc,30세,010-2222-3333,여자,서울,3,ccb,29세,x,여자,경기,9,dab,26세,x,남자,인천,8,aab,23세,010-3333-1111,여자,경기,10"

def resultPrint(resultDict,idx) :
    resultStr = "";
    for key in CONST_KEYS :
        resultStr += key + " : " + str(resultDict[key][idx]) + ", "

    print("할인 쿠폰을 받을 회원정보",end=" ")
    print(resultStr[:len(resultStr)-2])

def isValidation(resultDict) :
    checkLen = len(resultDict[CONST_KEYS[0]])
    for i in range(1,len(CONST_KEYS)) :
        nowLen = len(resultDict[CONST_KEYS[i]])
        if nowLen != checkLen : return False
    return True

def goodCustomer(aInfo) :
    resultDict = dict()

    try :
        # 회원정보 가공
        infoList = aInfo.split(",")
        for i in range(0,len(infoList)) :
            idx = i%len(CONST_KEYS)
            key = CONST_KEYS[idx]
            tempList = resultDict.get(key,list())
            tempList.append(int(infoList[i]) if infoList[i].isdigit() else infoList[i])
            resultDict[key] = tempList

        # 회원정보 개수 체크
        if not isValidation(resultDict) : raise

        # 전화번호 x 치환
        phones = resultDict[CONST_KEYS[2]]
        tempPhones = phones[:len(phones)]
        for i in range(0,len(phones)) :
            if phones[i] == 'x' : phones[i] = "000-0000-0000"
        resultDict[CONST_KEYS[2]]  = phones
        print(resultDict)

        # vip 찾기
        ranks = resultDict[CONST_KEYS[5]]
        for i in range(0,len(ranks)) :
            if ranks[i] >= 8 and tempPhones[i] != 'x' :
                resultPrint(resultDict,i)
    except :
        print("회원데이터가 잘못 되었습니다.")

goodCustomer(info)