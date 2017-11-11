class LinkedListElement :
    def __init__(self) :
        self.value = None
        self.myNext = None

class LinkedListPipe:
    '''
    Linked List를 이용하여 다음의 method들을 작성하세요.
    '''
    def __init__(self) :
        '''
        리스트 myPipe를 만듭니다. 이는 구슬의 배치를 저장합니다.
        '''
        #start는 링크드 리스트에서 맨 처음에 있는 애, end는 맨 마지막에 있는 애를 일컫음
        self.start = None #None은 텅 비어있다는 뜻을 의미함
        self.end = None
        pass

    def addLeft(self, n) :
        '''
        파이프의 왼쪽으로 구슬 n을 삽입합니다.
        '''
        if self.start == None :
            element = LinkedListElement()
            element.value = n
            element.myNext = None
            
            self.start = element
            self.end = element
        else:
            element = LinkedListElement()
            element.value = n
            element.myNext = self.start
            
            self.start = element

    def addRight(self, n) :
        '''
        파이프의 오른쪽으로 구슬 n을 삽입합니다.
        '''
        if self.start == None :
            element = LinkedListElement()
            element.value = n
            element.myNext = None
            self.start = element
            self.end = element
        else:
            element = LinkedListElement()
            element.value = n
            element.myNext = None
            
            self.end.myNext = element
            self.end = element

    def getBeads(self) :
        '''
        파이프의 배치를 list로 반환합니다.
        '''
        result = []
        
        cur = self.start
        
        while cur != None :
            result.append(cur.value)
            cur = cur.myNext
        
        return result

def processBeads(myInput) :
    '''
    구슬을 파이프에 넣는 행위가 myInput으로 주어질 때, 구슬의 최종 배치를 리스트로 반환하는 함수를 작성하세요.

    myInput[i][0] : i번째에 넣는 구슬의 번호
    myInput[i][1] : i번째에 넣는 방향

    예를 들어, 예제의 경우 

    myInput[0][0] = 1, myInput[0][1] = 0,
    myInput[1][0] = 2, myInput[1][1] = 1,
    myInput[2][0] = 3, myInput[2][1] = 0

    입니다.

    '''

    myPipe = LinkedListPipe()

    result = []

    for line in myInput :
        if line[1] == 0 :
            myPipe.addLeft(line[0])
        else :
            myPipe.addRight(line[0])
        
    return myPipe.getBeads()

def main():
    '''
    이 곳은 수정하지 마세요.
    '''

    n = int(input())

    myList = []

    for i in range(n) :
        myList.append([int(v) for v in input().split()])

    print(processBeads(myList))

if __name__ == "__main__":
    main()





"""

입력
입력의 첫 번째 줄에는 구슬의 개수 nn이 주어진다. 두 번째 줄부터는 토끼가 구슬을 넣는 행위가 주어진다. 각 줄은 두 개의 정수 aa, bb로 이루어지며, 이 뜻은 구슬 aa를 왼쪽 혹은 오른쪽으로 넣는다는 의미이다. (bb가 0이면 왼쪽, bb가 1이면 오른쪽이며 그 외의 입력은 주어지지 않는다)

출력
최종적으로 구슬이 파이프 속에서 어떻게 배치되어 있는지를 출력한다.

입력 예시
3
1 0
2 1
3 0

출력 예시
3 1 2

"""
