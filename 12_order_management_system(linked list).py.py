class listElem :
    def __init__(self, data, myPrev, myNext) :
        self.data = data
        self.myNext = myNext
        self.myPrev = myPrev

class orderManager :
    def __init__(self) :
        dummy = listElem(-1, None, None)

        self.begin = dummy
        self.end = dummy
        
        self.orderToElem = {}

    def removeItemId(self, orderId) :
        del self.orderToItem[orderId]

    def addOrder(self, orderId) :
        singleOrder = listElem(orderId, None, None)

        self.end.myNext = singleOrder
        singleOrder.myPrev = self.end

        self.end = singleOrder

        self.orderToElem[orderId] = singleOrder

    def removeOrder(self, orderId) :
        elem = self.orderToElem[orderId]

        prevElem = elem.myPrev
        nextElem = elem.myNext

        if prevElem != None :
            prevElem.myNext = nextElem

        if nextElem != None :
            nextElem.myPrev = prevElem

        if elem is self.end :
            self.end = prevElem

        del self.orderToElem[orderId]

    def getOrder(self, orderId) :
        cnt = 0

        cur = self.begin

        while cur != None :
            if cur.data == orderId :
                return cnt

            cur = cur.myNext
            cnt = cnt + 1

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

