def diffDigit(a, b) :
    '''
    a, b의 서로 다른 자리수의 개수를 반환한다
    '''

    result = 0

    while a != 0 or b != 0 :
        t1 = a % 10
        t2 = b % 10
        if t1 != t2 :
            result += 1
        a = a // 10
        b = b // 10
    return result;

def main():
    '''
    Do not change this code
    '''

    a = int(input())
    b = int(input())

    print(diffDigit(a, b))


if __name__ == "__main__":
    main()




""'
입력
첫 번째 줄과 두 번째 줄에 각각 자연수가 주어진다.

출력
각 자릿수의 숫자를 비교하여, 다른 자리수의 개수를 출력한다.

입력 예시 1
212
233

출력 예시 1
2

입력 예시 2
123
123456

출력 예시 2
6
"""
