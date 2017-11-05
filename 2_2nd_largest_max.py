def getMax2(n, myMatrix):
    '''
    크기 n x n 의 행렬 myMatrix내의 원소의 합, 최댓값, 두 번째 최댓값을 반환하는 함수.

    만약 myMatrix = [[1, 2, 3], [2, 3, 4], [3, 3, 4]]라면 (25, 4, 3) 을 반환한다.
    '''

    mySum = 0
    myMax = 0
    myMax2 = 0

    for matrix in myMatrix :
        for num in matrix :
            mySum += num
            if myMax2 < num :
                if myMax < num :
                    myMax2,myMax = myMax,num
                elif myMax > num :
                    myMax2 = num

    return (mySum, myMax, myMax2)

def main():
    '''
    이 부분은 수정하지 마세요.
    '''

    n = int(input())
    myMatrix = []

    for i in range(n):
        myMatrix.append([int(v) for v in input().split()])

    print(getMax2(n, myMatrix))

if __name__ == "__main__":
    main()








"""
입력: 첫번째 줄에는 nn이 주어집니다. 이어 nn개의 줄에 대하여 nnxnn 행렬의 원소가 주어집니다. 모든 원소는 양수라고 가정합니다.
출력: 1) 모든 원소의 합, 2) 원소의 최댓값, 3) 원소의 두 번째 최댓값을 차례대로 출력합니다. 두 번째 최댓값은 항상 존재한다고 가정합니다.

입력 예시 1
3
1 2 3
2 3 4
4 4 2

출력 예시 1
(25, 4, 3)

입력 예시 2
5
7 2 3 4 5
2 3 4 1 2
2 3 2 5 2
3 3 4 2 1
3 5 2 1 1

출력 예시 2
(72, 7, 5)
"""
