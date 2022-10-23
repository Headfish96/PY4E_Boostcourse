# Q3. 요즘 식당에 들어가면 방명록을 적게 되어있습니다.
# 어느 식당의 사장님이 여러분에게 방명록을 주면서 전화번호를 제대로 적었는지 검사해달라는 부탁을 했습니다.
# 아래와 같은 방명록이 있을 때 방명록을 잘 못쓴 사람의 이름과 잘 못된 번호를 출력하는 함수를 만들어 봅시다.

guest_book = """김갑,123456789
이을,010-1234-5678
박병,010-5678-111
최정,111-1111-1111
정무,010-3333-3333"""

import os
def wrong_number(n):
    c1 = n.startswith('010')
    c2 = len(n)==13
    c3 = n[3]=='-'
    c4 = n[8]=='-'
    if c1*c2*c3*c4 == 0:
        return n
    else: return None
        
def wrong_guest_book(a):
    if not os.path.exists("C:/python_study"):
        os.makedirs("C:/python_study")

    f = open("C:/python_study/guest_book.txt", 'w')
    f.write(guest_book)
    f.close()
    
    B = guest_book.split("\n")
    for b in B:
        name = b.split(',')[0]
        number = b.split(',')[1]
        if number == wrong_number(number):
            print("잘못 쓴 사람:",name)
            print("잘못 쓴 번호",number)
            print("""""")


wrong_guest_book(guest_book)