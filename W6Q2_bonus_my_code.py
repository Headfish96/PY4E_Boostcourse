"""
Q2.  여러분은 6명의 멤버를 거느리는 영업팀의 영업관리자 입니다. 각 멤버별로 올해 실적을 보고 잘한 멤버는 보너스를 주고 못한 멤버는 면담을 하려고 합니다. 파이썬을 이용하여 함수를 만들어 보너스 대상자와 면담 대상자를 골라주세요.

😲조건 1 - 예비 보너스 대상자는 평균 실적 1등 2등 입니다.
😲조건 2 - 예비 면담 대상자는 평균 실적 5등 6등 입니다.
😲조건 3 - 보너스 대상자의 평균 실적이 5보다 크지 않으면 보너스 대상자에서 제외 됩니다.
😲조건 4 - 면담 대상자의 평균 실적이 3보다 크면 면담 대상자에서 제외 됩니다.

# 이름, 실적
member_names = ["갑돌이", "갑순이", "을돌이", "을순이", "병돌이", "병순이"]
member_records = [[4,5,3,5,6,5,3,4,1,3,4,5],[2,3,4,3,1,2,0,3,2,5,7,2], 
           [1,3,0,3,3,4,5,6,7,2,2,1],[3,2,9,2,3,5,6,6,4,6,9,9],
           [8,7,7,5,6,7,5,8,8,6,10,9],[7,8,4,9,5,10,3,3,2,2,1,3]]
           

✅출력 예시
sales_management(member_names, member_records)
보너스 대상자 병돌이
보너스 대상자 을순이

면담 대상자 갑순이
"""

"""
    new_info = []
    for j in range(len(tsinfo)):
        new_info.append((tsinfo[j][i]))
    t.append(new_info)

chunk_size = len(member_records[0])


for i in range(len(member_records[0])):
    new_info = []
    for j in range(len(member_records)):
        new_info.append()
"""
member_names = ["갑돌이", "갑순이", "을돌이", "을순이", "병돌이", "병순이"]
member_records = [[4,5,3,5,6,5,3,4,1,3,4,5],[2,3,4,3,1,2,0,3,2,5,7,2],
           [1,3,0,3,3,4,5,6,7,2,2,1],[3,2,9,2,3,5,6,6,4,6,9,9],
           [8,7,7,5,6,7,5,8,8,6,10,9],[7,8,4,9,5,10,3,3,2,2,1,3]]

member_records_avg = []
for j in range(len(member_records)):
    member_records_avg.append(float("%0.2f" % (sum(member_records[j])/len(member_records[j]))))

sales_management = list(zip(member_names, member_records_avg))
sales_management.sort(key=lambda x: x[1], reverse=True)


sales_management_bonus = []
for i in range(len(sales_management)):
    if sales_management[i][1] > 5:
        sales_management_bonus.append(sales_management[i][0])


for i in range(len(sales_management_bonus)):
    print("보너스 대상자:", sales_management_bonus[i])


sales_management_interview = []
for i in range(len(sales_management)):
    if sales_management[i][1] <= 3:
        sales_management_interview.append(sales_management[i][0])

for i in range(len(sales_management_interview)):
    print("면담 대상자:", sales_management_interview[i])