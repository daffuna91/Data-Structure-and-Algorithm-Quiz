class orderManager :
    '''
    주문을 처리하는 class를 작성합니다.
    '''

    def __init__(self) :
        '''
        이 부분은 고치지 마세요.
        '''
        self.data = []

    def addOrder(self, orderId) :
        '''
        주문번호 orderId를 추가합니다.
        '''
        self.data.append(orderId)

    def removeOrder(self, orderId) :
        '''
        주문번호 orderId를 제거합니다.
        '''
        self.data.remove(orderId)

    def getOrder(self, orderId) :
        '''
        주문번호 orderId가 몇 번째로 처리될지를 반환합니다.

        만약 주문번호 orderId가 존재하지 않으면 -1을 반환합니다. 
        '''
        for i in range(len(self.data)):
            if self.data[i] == orderId:
                return i+1
                
        return -1

def main():
    manager = orderManager()

    '''
    테스트를 하고싶으면, 아래 부분을 수정합니다.
    '''

    manager.addOrder(1)
    manager.addOrder(2)
    manager.addOrder(3)
    manager.removeOrder(2)

    print(manager.getOrder(1))
    print(manager.getOrder(2))
    print(manager.getOrder(3))

if __name__ == "__main__":
    main()





"""
테스트
이번 문제는 테스트 케이스가 총 20개입니다. 테스트 케이스 1번부터 10번까지는 작성하신 주문관리 시스템이 제대로 동작하는지를 체크하며, 11번부터 20번까지는 작성하신 주문관리 시스템의 성능을 잽니다.
11번부터 15번까지는 주문 조회를 매우 많이 할 경우, 16번부터 20번까지는 주문 조회를 거의 하지 않을 경우입니다. 이 두 경우에 대하여 리스트를 활용한 구현과 링크드 리스트를 활용한 구현의 성능 차이를 보도록 합니다.

시스템 테스트 입력 1
manager.addOrder(1)
manager.addOrder(2)
manager.addOrder(4)
manager.removeOrder(2)

print(manager.getOrder(1)) 
print(manager.getOrder(4)) 

manager.addOrder(2)
manager.removeOrder(1)
manager.addOrder(1)

print(manager.getOrder(2))

시스템 테스트 출력 1
1
2
2

시스템 테스트 입력 2
manager.addOrder(4)
manager.addOrder(8)

print(manager.getOrder(8))

manager.addOrder(2)
manager.addOrder(1)
manager.removeOrder(4)

print(manager.getOrder(8))

manager.addOrder(59)
manager.addOrder(5959)

print(manager.getOrder(59))

시스템 테스트 출력 2
2
1
4

시스템 테스트 입력 3
manager.addOrder(2)
manager.removeOrder(2)
manager.addOrder(1818)
manager.addOrder(8282)
manager.addOrder(2255)
manager.addOrder(6515)
manager.removeOrder(1818)
manager.addOrder(486)

print(manager.getOrder(486))
print(manager.getOrder(3))

manager.addOrder(4860)

시스템 테스트 출력 3
4
-1

"""
