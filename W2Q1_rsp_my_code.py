import random

##내가 무엇을 낼 것인지 입력하면 그 값을 출력한 후 숫자로 변환
def take_my_rsp():
    my_rsp = input("가위 바위 보! / 가위, 바위, 보 중 하나를 입력해주세요")
    if my_rsp == "가위":
        print("나:", my_rsp)
        my_rsp = 1
    elif my_rsp == "바위":
        print("나:", my_rsp)
        my_rsp = 2
    else:
        print("나:", my_rsp)
        my_rsp = 3
    return (my_rsp)

##랜덤하게 컴퓨터가 무엇을 낼 것인지 결정하고 그 값이 결정되면 문자로 출력
def take_computer_rsp():
    computer_rsp = random.randint(1, 3)
    if computer_rsp == 1:
        print("컴퓨터: 가위")
    elif computer_rsp == 2:
        print("컴퓨터: 바위")
    else:
        print("컴퓨터: 보")
    return (computer_rsp)

##절댓값을 이용한 승자 판별 함수
def judge():
    difference_rsp = mrsp - crsp ##내가 낸 것의 값과 컴퓨터가 낸 것의 값의 차
    absv_rsp = abs(difference_rsp) ##값의 차를 절댓값으로 변환
    rsp_arrangement = [mrsp, crsp] ##나와 컴퓨터의 값을 배열로 저장

    if absv_rsp == 2: ##절댓값의 차리가 2가될 경우는 [가위, 보]의 경우이다
        if min(rsp_arrangement) == mrsp: #1과 3중 최솟값인 1을 낸, 즉, 가위를 낸 사람의 승리
            print("나의 승리")
        else:
            print("컴퓨터의 승리")
    elif absv_rsp == 1: ##절댓값이 1이 되는 경우 큰 값을 낸 사람의 승리
        if max(rsp_arrangement) == mrsp:
            print("나의 승리")
        else:
            print("컴퓨터 승리")
    else: ##절댓값이 0인 경우 무승부
            print("무승부")

mrsp = take_my_rsp()
crsp = take_computer_rsp()

judge()