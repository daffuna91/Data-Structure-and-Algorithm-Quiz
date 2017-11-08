def getDivisorEasy(n, k):
    '''
    숫자 n의 k번째 약수를 반환하는 프로그램을 작성하세요.
    '''

    result = 0

    for i in range(1,n+1) :
        if n % i == 0 :
            k -= 1
        if k == 0 :
            result = i
            break

    return result

def main():
    '''
    Do not change this code
    '''

    line = [int(x) for x in input().split()]

    print(getDivisorEasy(line[0], line[1]))


if __name__ == "__main__":
    main()




"""
입력
첫 번째 줄에 숫자 nn과 kk가 주어진다.

출력
kk번째 약수를 출력한다. 만약 kk번째 약수가 존재하지 않을 경우에는 0을 출력한다.

입력 예시
6 3

출력 예시
3
"""
