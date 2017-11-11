class maxMachine : #max라는 주머니(class)가 있다. 이는 4개의 역할(def)을 할 수 있다.
    def __init__(self) :
        self.myData = [] #2) 주머니가 하나 생김

    def addNumber(self, n) :
        self.myData.append(n) #3)이 주머니에 하나 붙이는 것
#self를 쓰는 이유는 인스턴스 때문에

    def removeNumber(self, n) :
        self.myData.remove(n) #4)그리고 이 주머니에서 하나 빼는것
    def getMax(self) :
        return max(self.myData) #5) 주머니에서 제일 큰 것을 빼고

def main():

    myMachine = maxMachine() #1) 인스턴스가 생기자 마자

    '''
    테스트를 하고싶으면, 아래 부분을 수정합니다.
    '''

    myMachine.addNumber(1)
    myMachine.addNumber(2)
    myMachine.addNumber(3)
    myMachine.addNumber(2)

    print(myMachine.getMax())

    myMachine.removeNumber(3)

    print(myMachine.getMax())

    myMachine.removeNumber(2)

    print(myMachine.getMax())

if __name__ == "__main__":
    main()





"""
example


myMachine.addNumber(1)
myMachine.addNumber(2)
myMachine.addNumber(3)
myMachine.addNumber(2)

print(myMachine.getMax())

myMachine.removeNumber(3)

print(myMachine.getMax())

myMachine.removeNumber(2)

print(myMachine.getMax())

myMachine.removeNumber(2)

print(myMachine.getMax())

"""
