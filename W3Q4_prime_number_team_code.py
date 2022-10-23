# Q4. 2개의 숫자를 입력하여 그 사이에 소수가 몇 개인지 출력하는 함수를 만들어 봅시다.

# 제곱근을 사용하여 루프를 줄이는 알고리즘이 아닌 전체루프로 구현한 방법으로 취합하였습니다.
# 개발자의 생각이 가장 많이 묻어 있다고 판단하여 Q4문제를 해당 코드로 취합 하였습니다.
def prime_number(n, m) :
    # 변수 할당
    count = 0
    num = 0
    prime_count = 0

    # n과 m 중 큰 값과 작은 값에 따라 배열 할당
    if 1 < n < m :
        count = m - n + 1
        numbers = [ i for i in range(n, m+1)]
        # array debugging
        #print(numbers)
    elif 1 < m <= n :
        count = n - m + 1
        numbers = [ i for i in range(m, n+1)]
        # array debugging
        #print(numbers)

    while num < count :
        # while 문 안에서 작동할 변수 할당
        divisor = 1
        prime = 0

        while divisor < numbers[num] + 1 :
            # 나머지가 0이면 divisor를 약수로 가진다.
            if (numbers[num] % divisor) == 0 :
                prime = prime + 1
            
            divisor = divisor + 1
        
        # 약수를 1과 자기 자신 2개만 가지면 소수!
        if prime < 3 :
            prime_count = prime_count + 1

        # 소수와 소수가 아닌 수를 표시하는 Debugging Code
        #if prime > 2 :
        #    print(numbers[num], '은 소수가 아닙니다.')
        #else :
        #    print(numbers[num], '은 소수입니다.')
        #    prime_count = prime_count + 1
        
        num = num + 1
    
    if prime_count == 0 :
        print('입력 오류입니다!')
    else :
        
        print('소수 개수 :', prime_count)
        
try :
    print('1보다 큰 두 수를 입력하세요.')
    n = int(input('첫 번째 수 입력 : '))
    m = int(input('두 번째 수 입력 : '))
    print('------------결과------------')
    prime_number(n,m)
except :
    print('입력 오류입니다!')