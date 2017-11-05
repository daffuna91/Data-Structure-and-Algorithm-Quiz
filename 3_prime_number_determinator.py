import math

'''
다음의 함수들은 math 내의 함수들입니다. 참고하도록 합니다. 반드시 이 모든 함수를 써야한다는 의미는 아닙니다.

math.sqrt(x) : 루트 x를 반환
math.log(x) : 자연로그 x를 반환
math.log10(x) : 상용로그 x를 반환
'''

def isPrime(n):
    '''
    숫자 n이 소수이면 True, 아니면 False를 반환하는 함수
    '''
    for i in range(2,int(math.sqrt(n)+1)) :
        if n%i == 0 :
            return False

    return True

def main():
    '''
    이 부분은 수정하지 마세요.
    '''

    n = int(input())

    print(isPrime(n))

if __name__ == "__main__":
    main()





"""
입력: 첫번째 줄에는 nn이 주어집니다.
출력: nn이 소수라면 True, 아니면 False를 출력합니다.

입력 예시 1
7

출력 예시 1
True

입력 예시 2
16

출력 예시 2
False
"""
