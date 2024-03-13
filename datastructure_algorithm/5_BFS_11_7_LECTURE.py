#지난 시간 이진 트리 최대 2개의 자식 노드 
#너비우선순회: 큐 구조 이용> 소멸자에 적용하면 된다? 
'''
 트리를 구성할 후위 수식: A B * C D / -
 Levelorder: - * / A B C D

 빈 큐 생성 
 큐에 최상위 루트노드 넣고 시작 
 비어있지 않을 동안 하나씩 빼서 방문
 Queue가 비었으면 끝 
'''


# 연산자 여부 판단
def isOperator(op) -> bool :
    return op == '+' or op == '-' or op == '*' or op == '/'

class DNode :
    def __init__ (self, data, Llink=None, Rlink=None):
        self.data = data
        self.Llink = Llink
        self.Rlink = Rlink

class LinkedBTree : #이진트리 생성: 링크연결시켜서 후위 수식의 링크를 다 만들어준다.
    def __init__(self):
        self.__root = None
	    
    # 이진 트리(수식 트리) 생성: 스택 구조 활용    
    def makeLinkedBTree(self, postfix):
        postfix=postfix.replace('+',' + ')
        postfix=postfix.replace('-',' - ')
        postfix=postfix.replace('*',' * ')
        postfix=postfix.replace('/',' / ')
        postfix=postfix.split()

        S=[] 
        for st in postfix: #****후위 표기로 이미 변환된 식을 받는다고 해서 계산 
            # 3 5 * 6 2 / - (원래 식: 3*5 - (6/2))
            temp=DNode(st) #각각을 노드로 구성
            if isOperator(st): #연산자라면(스택 구조 생각해보자 왼쪽에 들어가는게 더 아래쪽에 stack> pop한 값은 Rlink로 해줘야함 )
                temp.Rlink=S.pop() #피연산자 pop해서 연결
                temp.Llink=S.pop()

            S.append(temp) #operand 노드를 그냥 push #operator의 경우 위에서 L, R연결한 후에 append함. 
        #결론적으로 전체 트리 구조 다 만들어짐
        self.__root=S.pop() #루트 노드 (마지막 연산자) pop해서 root노드로 설정 
    # 깊이 우선 순회: 전위.중위.후위 순회    
    def Preorder_(self): # <------반복적 용법
        S=[] #스택으로 구현 
        node=self.__root #루트 노드로 설정 
        while S or node:
            if node:
                print(node.data, end=' ')               #루트노드 
                S.append(node) #스택에 append시켜놔야 Llink없을 때 부모노드로 돌아갈 수 있다 #왼쪽서브트리
                node=node.Llink #Llink로 이동함 
            else: 
                node=S.pop().Rlink #Llink가 없다면 이전루트를 pop해서 오른쪽 서브트리 
    def Preorder(self): #<---------재귀적 용법
        def _Preorder(tNode):
            if tNode: # 11/7 이 부분 계속 오류 못잡음!! 코드핵심
                print(tNode.data, end=' ')
                _Preorder(tNode.Llink)
                _Preorder(tNode.Rlink)
        _Preorder(self.__root)
    #함수 선언하고 그 안에 함수 또 선언해야 함
    #내가 구상했던 코드 아래와 같음 
    #재귀적용법: 간단하게 한번의 사이클만 생각하자!!!!!!!너무 복잡하게x
    '''

    def Preorder(self):
        temp=DNode(self.__root)
        print(temp.data, end=' ')
        Preorder(temp.Llink)
        Preorder(temp.Rlink)
    문제점: preorder함수 매개변수로 넘겨줄게 없다.
    맨처음 Preorder호출시에도 사용자가 root를 입력하진 않을 것 
    ''' 
    def Inorder_(self): #<---------반복적 용법
        S = []  # 스택 생성
        node = self.__root  

        while S or node:
            if node:
                S.append(node)  # 현재 노드를 스택에 저장
                node= node.Llink  # Llink끝까지 이동 
            else:
                node = S.pop()  # Llink없으면 pop 
                print(node.data, end=' ') #출력
                node = node.Rlink  # 오른쪽 자식 노드로 이동

    def Inorder(self): #<----------재귀적 용법 
        def _Inorder(tNode):
            if tNode:
                _Inorder(tNode.Llink) 
                print(tNode.data, end=' ')
                _Inorder(tNode.Rlink)
        _Inorder(self.__root)
           
    def Postorder_(self): #<----------반복적 용법 
        S = []  # 노드를 저장할 스택 생성
        result = []  # 방문한 노드를 저장할 리스트 생성
        node = self.__root  # 현재 노드를 루트로 설정

        while S or node:
            if node:
                S.append(node)  # 현재 노드를 스택에 저장
                result.insert(0, node.data)  # 결과 리스트에 현재 노드 데이터를 처음에 삽입하여 역순으로 저장
                node = node.Rlink  # 오른쪽 자식 노드로 이동
            else:
                node = S.pop().Llink  # 스택에서 노드를 꺼내서 왼쪽 자식 노드로 이동

        for item in result:
            print(item, end=' ')  # 결과 리스트를 출력하여 후위 순회 결과를 얻습니다.

    def Postorder(self): #<---------재귀적 용법 
        def _Postorder(tNode):
            if tNode:
                _Postorder(tNode.Llink)
                _Postorder(tNode.Rlink)
                print(tNode.data, end=' ')
        _Postorder(self.__root)
    
	    
    # 너비 우선 순회: 비재귀적 용법(큐 구조 활용) Lv0부터 출력함!! 아래서위로 올라가는게 아님!!
    def Levelorder(self):
        tempQ=[]
        tempQ.append(self.__root)
        while len(tempQ):
            tNode=tempQ.pop(0) #큐 구조 -1이 아닌 0을 pop해야 함 
            print(f'{tNode.data}', end=' ')
            if tNode.Llink:  #Llink의 존재 여부 자체로 if 문으로 넣어버리면 된다!
                tempQ.append(tNode.Llink) #if None객체가 아니라면 append
            if tNode.Rlink:
                tempQ.append(tNode.Rlink) 
            #root를 방문하고 L, R 을 스택에 삽입 
            #R을 


    def __del__(self):      # 소멸자: 이진 트리의 모든 노드 삭제
        #temp=DNode(self.__root) self.__root자체가 노드임 
        Q=[]
        Q.append(self.__root)
        while len(Q):
            tNode=Q.pop(0)
            if tNode.Rlink:
                Q.append(tNode.Rlink)
            if tNode.Llink:
                Q.append(tNode.Llink)
            del tNode #해당 노드에 대한 참조를 해제해버림 


# from LinkedBTree import LinkedBTree   
if __name__ == '__main__':     
    postfix = input('트리를 구성할 후위 수식: ')
    BT = LinkedBTree()
    BT.makeLinkedBTree(postfix)
    # root = BT.makeLinkedBTree(postfix)

    # 이진 트리 깊이 우선 순회: 전위.중위.후위 순회
    print('Preorder  : ', end=' ');     BT.Preorder_();    print('')
    print('Inorder   : ', end=' ');     BT.Inorder_();     print('')
    print('Postorder : ', end=' ');     BT.Postorder_();   print('')
    # 이진 트리 너비 우선 순회
    print('Levelorder : ', end=' ');    BT.Levelorder();  print('')

