# Q2. 어느날 여러분이 어떤 글을 읽고 있는데, 갑자기 특정 글자가 전체 글에서 몇개 들어있는지 궁금해졌습니다. 그럼 한 번 파이썬 함수로 만들어 봅시다.
full_text = """
녹둔도 전투, 첫 번째 백의종군

수책거적도(守柵拒敵圖)
1587년(선조 20년) 조산보만호 겸 녹도 둔전사의 이순신에게 녹둔도의 둔전을 관리하도록 하였다. 그해 가을에는 풍년이 들었다. 그해 9월 1일 이순신이 경흥부사 이경록과 함께 군대를 인솔하여 녹둔도로 가서 추수를 하는 사이에 추도에 살고 있던 여진족이 사전에 화살과 병기류를 숨겨놓고 있다가, 기습 침입하여 녹둔도 전투가 벌어졌다. 녹둔도 전투에서 조선군 11명이 죽고 160여 명이 잡혀갔으며, 열다섯 필의 말이 약탈당했다. 하지만 이일이 도망치는 와중에 이순신은 이경록과 남아서 싸웠고 그 결과 승리했으며 조선인 백성 60여 명을 구출했다. 이 과정에서 이순신의 무예는 대단했는데 고작 수십명의 병사들로 1,000기의 여진족 기병을 상대로 방어에 성공했으며 반격하여 무찔렀다.

당시 조산만호 이순신은 북방 여진족의 약탈 및 침략을 예상하고 수비를 강화하기 위하여 여러차례 북병사 이일에게 추가 병력을 요청하였으나, 모두 거절 당하였다. 이 패전으로 인해 책임을 지게 된 북병사 이일은 이순신에게 그 책임을 덮어 씌우고 이순신은 죄를 받아 수금되었고 백의종군(白衣從軍)하게 되었다.

전투의 결과를 북병사 이일(李鎰)은 녹둔도 함몰이라고 비판하였다. 처음부터 군사 10명이 피살되고 106명이 포로가 되었으며 말 15필을 빼앗기는 등의 피해가 많았다 하여 이 녹둔도 사건으로 인해서 함경도 북병사 이일(李鎰)의 비판으로 문책받고 그해 10월 해임, 결국 투옥되었다. 북병사 이일은 이경록과 이순신을 투옥한 뒤, 1587년 10월 10일 "적호(賊胡)가 녹둔도의 목책(木柵)을 포위했을 때 군기를 그르쳤다"고 장계를 올려 이를 보고하였다.
"""

import os
FILE_NAME = "week4.txt"
FILE_PATH = "C:/study/python"
def count_word(text,findWord) :
    try :
        if not os.path.exists(FILE_PATH):
            os.makedirs(FILE_PATH)

        fopen = open(FILE_PATH + "/" + FILE_NAME,"w")
        fopen.write(text)
    except :
        print("error : count_word() 오류발생하였습니다.")
    finally :
        try : fopen.close() 
        except : pass

    return text.count(findWord)
    
print(count_word(full_text,"이순신"))