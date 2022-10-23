"""
Q4. 여러분은 어떤 상품을 판매하고 있습니다. 매월 상품을 많이 구매해준 VIP회원에게 할인 쿠폰을 제공해주려고 합니다.
아래와 같은 회원 정보가 있을 때 회원 정보를 출력하고 할인 쿠폰을 받을 회원이 누구인지 출력하는 함수를 만들어 주세요.
😲조건1 - 8회 이상 구매한 회원이 VIP대상
😲조건2 - 전화번호가 없으면 쿠폰을 받을 수 없음
😲조건3 - 전화번호가 없으면 000-0000-0000으로 출력할 것

# 6명의 회원이고 "아이디,나이,전화번호,성별,지역,구매횟수" 순서로 입력되어 있음
info = "abc,21세,010-1234-5678,남자,서울,5,
        cdb,25세,x,남자,서울,4,
        bbc,30세,010-2222-3333,여자,서울,3,
        ccb,29세,x,여자,경기,9,
        dab,26세,x,남자,인천,8,
        aab,23세,010-3333-1111,여자,경기,10"

✅출력 예시
good_customer(info)
{'아이디': ['abc', 'cdb', 'bbc', 'ccb', 'dab', 'aab'], 
'나이': ['21세', '25세', '30세', '29세', '26세', '23세'], 
'전화번호': ['010-1234-5678', '000-0000-0000', '010-2222-3333', '000-0000-0000', '000-0000-0000', '010-3333-1111'], 
'성별': ['남자', '남자', '여자', '여자', '남자', '여자'], 
'지역': ['서울', '서울', '서울', '경기', '인천', '경기'], 
'구매횟수': [5, 4, 3, 9, 8, 10]}
할인 쿠폰을 받을 회원정보 아이디:aab, 나이:23세, 전화번호:010-3333-1111, 성별:여자, 지역:경기, 구매횟수: 10
"""
info = "abc,21세,010-1234-5678,남자,서울,5, cdb,25세,010-5284-4649,남자,서울,4, bbc,30세,010-2222-3333,여자,서울,3, ccb,29세,010-6422-7410,여자,경기,9, dab,26세,010-6329-7410,남자,인천,8, aab,23세,010-3333-1111,여자,경기,10"
ninfo = info.replace(" ", "")
#print(ninfo)
ninfo.split(',')
sinfo: list = ninfo.split(',')

chunk_size = 6
tsinfo = []
for i in range(0, len(sinfo), chunk_size):
    tsinfo.append(sinfo[i:i + chunk_size])

vip_info = []
for i in range(len(tsinfo)):
    if int(tsinfo[i][5]) > 7:
        vip_info.append(tsinfo[i])
    else:
        continue

id_vip_info = []
age_vip_info = []
phone_vip_info = []
sex_vip_info = []
location_vip_info = []
times_vip_info = []
new_info = []
t = []

for i in range(chunk_size):
    new_info = []
    for j in range(len(tsinfo)):
        new_info.append((tsinfo[j][i]))
    t.append(new_info)


winner_vip = []
for i in range(len(vip_info)):
    if vip_info[i][3] != 'x':
        winner_vip.append(vip_info[i])
    else:
        continue

print("아이디:", t[0])
print("나이:", t[1])
print("전화번호:", t[2])
print("성별:", t[3])
print("지역:", t[4])
print("구매횟수:", t[5])
print("할인 쿠폰을 받을 회원정보:")
print(winner_vip)
