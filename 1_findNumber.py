def findNumber(myList, m):
    '''
    myList 내에 숫자 m이 존재하면 True, 아니면 False를 반환하는 함수

    만약 myList = [1, 3, 2, 5, 4]이고, m = 7이라면 False를 반환한다.
    '''
    return m in myList

def main():
    '''
    이 부분은 수정하지 마세요.
    '''

    myList = [int(v) for v in input().split()]
    m = int(input())

    print(findNumber(myList, m))

if __name__ == "__main__":
    main()
    
# 입력: 첫번째 줄에는 nn개의 숫자가 주어집니다. 두번째 줄에는 숫자 mm이 주어집니다.
# 출력: nn개의 숫자 중에서 mm이 존재하면 True를, 그렇지 않으면 False를 반환합니다.    

#입력 예시 1
#3 4 2 5 1 2 3 
#1
#출력 예시 1
#True

#입력 예시 2
#1 2 3 4 5 6
#7
#출력 예시 2
#False
