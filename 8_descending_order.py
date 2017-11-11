#Instructions: http://www.evernote.com/l/ACgUzetkv4tAfLDEkb0gNWe_sRjTjAyJm1w/

class maxMachine :
    def __init__(self) :
        self.myData = []

    def addNumber(self, n) :
        self.myData.append(n)

    def removeNumber(self, n) :
        self.myData.remove(n)

    def getMax(self) :
        return max(self.myData)


def sorting(myList) :
    '''
    myList를 내림차순으로 정렬하여 반환하는 함수를 작성하세요.

    예를 들어, myList = [5, 2, 3, 1] 이라면 [5, 3, 2, 1] 을 반환해야 합니다.

    단, maxMachine class를 이용하도록 합니다.
    '''

    myMachine = maxMachine()

    result = []

    for element in myList :
        myMachine.addNumber(element)

    for i in range(len(myList)) :
        myMax = myMachine.getMax()

        result.append(myMachine.getMax())
        myMachine.removeNumber(myMax)

    return result

def main():
    '''
    이 곳은 수정하지 마세요.
    '''

    myList = [int(v) for v in input().split()]

    print(sorting(myList))

if __name__ == "__main__":
    main()







"""
입력
숫자들이 주어집니다.

출력
숫자들을 내림차순으로 정렬하여 출력합니다.

입력 예시
2 5 1 4 4 3 2

출력 예시
[5, 4, 4, 3, 2, 2, 1]
"""
