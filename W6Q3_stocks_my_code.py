stocks = '삼성전자/10/85000,카카오/15/130000,LG화학/3/820000,NAVER/5/420000'
sells = [82000, 160000, 835000, 410000]
a = stocks.split(',')

stock = []
benefit = []
pbenefit = []
subject = []

for i in range(len(a)):
    stock.append(a[i].split('/'))
    subject.append(stock[i][0])
    benefit.append(((int(stock[i][1]) * int(sells[i]) - int(stock[i][1]) * int(stock[i][2])) / (
                int(stock[i][1]) * int(stock[i][2]))) * 100)
    pbenefit.append(float("%0.2f" % benefit[i]))

tbenefit = list(zip(subject, pbenefit))

print(stock)
print(benefit)
print(pbenefit)
print(tbenefit)

tbenefit.sort(key=lambda x: x[1], reverse=True)
print(tbenefit)