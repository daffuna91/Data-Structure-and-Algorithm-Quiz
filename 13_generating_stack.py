class Stack:
    '''
    List를 이용하여 다음의 method들을 작성하세요.
    '''
    def __init__(self) : #__init__함수는 instance가 만들어질 때 구현되는 함수임
        '''
        스택 myStack을 만듭니다.
        '''
        self.myStack = []

    def push(self, n) :
        '''
        stack에 정수 n을 넣습니다.
        '''
        self.myStack.append(n)

    def pop(self) :
        '''
        stack에서 가장 위에 있는 정수를 제거합니다. 만약 stack에 아무 원소가 없다면 아무 일도 하지 않습니다.
        '''
        #스택이 비어있는지 비어있지 않은지를 확인하기 위해서는 stack안에 있는 원소개수를 통해서 이를 알 수 있음
        if len(self.myStack) == 0:
            return
        else:
            self.myStack.pop()
            #리스트 내에 맨 오른쪽(마지막) 인수를 빼주고, 길이까지 줄여주는 함수 = pop

    def size(self) :
        '''
        stack에 들어 있는 정수의 개수를 return 합니다.
        '''
        return len(self.myStack)

    def empty(self) :
        '''
        stack이 비어있다면 1, 아니면 0을 return 합니다.
        '''
        if len(self.myStack) == 0:
            return 1
        else:
            return 0

    def top(self) :
        '''
        stack의 가장 위에 있는 정수를 return 합니다. 만약 stack에 들어있는 값이 없을 경우에는 -1을 return 합니다.
        '''
        if len(self.myStack) == 0:
            return -1
        else:
            return self.myStack[-1]
            #python에서 [-1]은 제일 마지막 원소를 지칭함

def main():
    stack = Stack()

    '''
    테스트를 하고싶으면, 아래 부분을 수정합니다.
    '''
    stack.push(1)
    stack.push(2)
    stack.push(4)
    stack.pop()

    print(stack.size()) 
    print(stack.top())


if __name__ == "__main__":
    main()





"""
테스트

시스템 테스트 입력 1

    stack.push(1)
    stack.push(2)
    stack.pop()
    stack.push(4)
    stack.pop()

    print(stack.size()) 
    print(stack.top())
    print(stack.empty())


시스템 테스트 출력 1

1
1
0



시스템 테스트 입력 2

    stack.push(3)
    stack.pop()
    stack.pop()

    print(stack.size()) 
    print(stack.top())
    print(stack.empty())


시스템 테스트 출력 2

0
-1
1
"""
