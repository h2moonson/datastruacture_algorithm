#binary tree practice
#입력받은 후위표기 수식을 트리 구조로 만들어두자! 
def isOperator(op):
    return op=='+' or op=='-' or op=='*' or op=='/'

class TreeNode: #각 노드의 구조 정의
    def __init__(self,data,Llink=None, Rlink=None):
        self.data=data
        self.Llink=Llink
        self.Rlink=Rlink
class LinkedBTree: #전체 트리의 구조 설계 > 여기 안에 전위순회,중위순회,후위순회 멤버함수로 클래스 내부에 구현해야한다..
    def __init__(self):
        self.__root=None
    def makeLinkedBTree(self, postfix)->TreeNode:
        postfix=postfix.replace('+',' + ')
        postfix=postfix.replace('-',' - ')
        postfix=postfix.replace('*',' * ')
        postfix=postfix.replace('/',' / ')
        postfix=postfix.split()
        #data에 각각의 연산자나 피연사자를 하나씩 넣어야한다.
        #split으로 쪼개준다

        S=[] 
        for st in postfix: #****후위 표기로 이미 변환된 식을 받는다고 해서 계산 
            # 3 5 * 6 2 / - (원래 식: 3*5 - (6/2))
            temp=TreeNode(st) #각각을 노드로 구성 data에 넣는다
            if isOperator(st): #연산자라면
                temp.Rlink=S.pop() #피연산자 pop해서 연결
                temp.Llink=S.pop()

            S.append(temp) #operand 노드를 push #operator의 경우 위에서 다 연결한 후에 append함. 그럼 트리구조가 갖춰진 상태

        self.__root=S.pop() #루트 노드 >최종적인 마지막 연산자. 후위 표기의 맨 마지막
    
    def Preorder(self):
        def _Preorder(tNode): #함수 정의
            if tNode:  #자식노드가 있다면 아래 실행 없다면 아무것도 실행하지 않음
                print(tNode.data, end=' ')#데이터를 출력하고 
                _Preorder(tNode.Llink)#Llink로 다음 노드
                _Preorder(tNode.Rlink)
        _Preorder(self.__root)  #함수 시작은 결국 루트 노드 부터! 

    def Inorder(self):
        def _Inorder(tNode):
            if tNode: 
                _Inorder(tNode.Llink)
                print(tNode.data, end= ' ')
                _Inorder(tNode.Rlink)
        _Inorder(self.__root)

    def Postorder(self):
        def _Postorder(tNode):
            if tNode:
                _Postorder(tNode.Llink)
                _Postorder(tNode.Rlink)
                print(tNode.data, end=' ')
        _Postorder(self.__root)


if __name__ == '__main__':     
    postfix = input('트리를 구성할 후위 수식: ')
    BT = LinkedBTree()
    BT.makeLinkedBTree(postfix) #이 함수가 실행되면서 링크가 연결되며 트리 구성 > Root노드도 정의됨

    # root = BT.makeLinkedBTree(postfix)

    # 이진 트리 깊이 우선 순회: 전위.중위.후위 순회
    print('Preorder  : ', end=' ');     BT.Preorder();    print('')
    print('Inorder   : ', end=' ');     BT.Inorder();     print('')
    print('Postorder : ', end=' ');     BT.Postorder();   print('')

    # 이진 트리 너비 우선 순회
    #print('Levelorder : ', end=' ');    BT.Levelorder();  print('')