# Q2. 가위바위보 업그레이드 버젼을 함수로 만들어 봅시다. 아래와 같은 조건을 만족해 주세요.

import random

CONSTANT_ERR_MSG = "입력값 오류입니다. 다시 입력해주세요."

gWin = [0] * 3
# 내가 무엇을 낼 것인지 입력하면 그 값을 출력한 후 숫자로 변환
def take_my_rsp():
    my_rsp = input("가위 바위 보! / 가위(1), 바위(2), 보(3) 중 하나를 입력해주세요.(종료=quit) : ")
    if my_rsp == "quit" : return -1  # 게임 강제종료

    if my_rsp == "가위" or my_rsp == "1" :
        print("나: 가위")
        my_rsp = 1
    elif my_rsp == "바위" or my_rsp == "2" :
        print("나: 바위")
        my_rsp = 2
    elif my_rsp == "보" or my_rsp == "3" :
        print("나: 보")
        my_rsp = 3
    else:
        my_rsp = 4
        
    return (my_rsp)


# 랜덤하게 컴퓨터가 무엇을 낼 것인지 결정하고 그 값이 결정되면 문자로 출력
def take_computer_rsp():
    computer_rsp = random.randint(1, 3)
    if computer_rsp == 1:
        print("컴퓨터: 가위")
    elif computer_rsp == 2:
        print("컴퓨터: 바위")
    else:
        print("컴퓨터: 보")
    return (computer_rsp)


# 절댓값을 이용한 승자 판별
def judge(mrsp, crsp):
    difference_rsp = mrsp - crsp  # 내가 낸 것의 값과 컴퓨터가 낸 것의 값의 차
    absv_rsp = abs(difference_rsp)  # 값의 차를 절댓값으로 변환
    rsp_arrangement = [mrsp, crsp]  # 나와 컴퓨터의 값을 배열로 저장

    if absv_rsp == 2:  # 절댓값의 차리가 2가될 경우는 [가위, 보]의 경우이다
        if min(rsp_arrangement) == mrsp:  # 1과 3중 최솟값인 1을 낸, 즉, 가위를 낸 사람의 승리
            gWin[0] = gWin[0] + 1
            print("나의 승리",end="\n\n")
        else:
            cwin = cwin + 1
            print("컴퓨터의 승리",end="\n\n")
    elif absv_rsp == 1:  # 절댓값이 1이 되는 경우 큰 값을 낸 사람의 승리
        if max(rsp_arrangement) == mrsp:
            gWin[0] = gWin[0] + 1
            print("나의 승리",end="\n\n")
        else:
            gWin[1] = gWin[1] + 1            
            print("컴퓨터 승리",end="\n\n")
    else:  # 절댓값이 0인 경우 무승부
        gWin[2] = gWin[2] + 1
        print("무승부",end="\n\n")


# 가위 바위 보 진행
def play():
    while True:  # 가위, 바위, 보 이외에 다른 입력을 받으면 재입력
        try :
            mrsp = take_my_rsp()
            if mrsp in [1, 2, 3] :
                crsp = take_computer_rsp()
                judge(mrsp, crsp)
                break
            elif mrsp == -1 :
                return False
            else :
                raise
        except :
            print(CONSTANT_ERR_MSG)

    return True


def game():
    while True:
        try :
            input_num_game = input("몇 판을 하시겠습니까?(종료=quit) ")
            if input_num_game == "quit" : return

            input_num_game = int(input_num_game)
            if input_num_game > 0:
                break
            else:
                raise
        except :
            print(CONSTANT_ERR_MSG)
      
    for i in range(input_num_game):
        i = i + 1
        print("**********************************************")
        print("{}번째 판".format(i))
        if play() == False : break
        
game()
print("나의 전적: {}승 {}무 {}패".format(gWin[0], gWin[2], gWin[1]))
print("컴퓨터의 전적: {}승 {}무 {}패".format(gWin[1], gWin[2], gWin[0]))