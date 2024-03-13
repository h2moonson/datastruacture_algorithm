#BST practice 11_25.py
class DNode: #기본 노드의 구조를 정의, data, Llink, Rlink
    def __init__(self,data,Llink=None,Rlink=None):
        self.data=data
        self.Llink=Llink
        self.Rlink=Rlink
 #전체 자료구조를 정의 > root는 필수 root를 기준으로 삽입을 하거나 삭제를 하낟.
class BSTree:
    def __init__(self):
        self.__root=None
    
    #[탐색] 재귀적 용법으로 구현, 루트노드와 찾는 데이터를인자로 넘겨서 비교
    def search(self,data):
        return self.__searchBST(self.__root,data)
    def __searchBST(self,tNode:DNode, data):
        if (tNode==None): return None  
        #얘는 맨 마지막에 발생 
        # 단말노드의 자식이없다> 거기까지 갔는데도 data==tNode.data실패> 탐색실패
        elif (data==tNode.data): return tNode
        elif (data<tNode.Llink): #크기비교해서 Llink재귀적으로 타고내려가도록
            return self.__searchBST(tNode.Llink,data) 
        else: #Rlink타고 내려가도록
            return self.__searchBST(tNode.Rlink,data)
        
    def SearchBST(self): #비재귀적 용법   
    # main문에서 삽입, 삭제, 검색,출력을 받고 검색하면 SearchBST실행
    # mina문에서 print문 안하고 SearchBST안에서 실행시킨 것 
    # _searBST는 SearchBST내부에 정의> 밑에 while문 실행되어 검색할 데이터를 받고
    #그제서야 호출이 된다. 
        def _searchBST(root,data): # *Llink Rlink타고 내려가면서 기준이 되는 Root값을 수정할 것 
            while root!=None:
                if data==root.data: return root
                elif data< root.data: root=root.Llink
                else: root=root.Rlink
            if root==None: return None
        if not self.__root: 
            print("\n 데이터가 존재하지 않습니다.")
            return
        print("\n 이진 검색 트리: 데이터 검색")
        while True:
            num=int(input('임의의 정수 입력(종료:0): '))
            if num==0 : break
            tNode=_searchBST(self.__root,num)
            if tNode : print(f'{tNode.data} 키를 찾았습니다.! ')
            else: print('키를 찾지 못했습니다.')
    #[삽입] 데이터삽입을 재귀적 용법으로 구현 >루트노드와 삽입할데이터를 인자로
    #반환값은 삽입할 위치의 노드 
    def insert(self,data):
        self.__root=self.__insertBST(self.__root,data)
    #값을 비교하면서 루트노드의 데이터보다 작을 경우 
    #루트노드의Llink를 루트로 해서 탐색 
    #return tNode가 헷갈리면 10 번슬라이드 필기를 봐라! 
    def __insertBST(self,tNode, data)->DNode:
        if(tNode==None): 
            tNode=DNode(data,None,None) 
            #아예 맨 처음이거나/ 단말노드까지 내려간 경우==검색실패위치==삽입위치 
            #데이터,Llink=None,Rlink=None으로 
        elif (data<tNode.data):
            tNode.Llink=self.__insertBST(tNode.Llink,data)
        else: 
            tNode.Rlink=self.__insertBST(tNode.Rlink,data)
        return tNode
     #**여기가 중요!! 맨 처음 if 문에 걸리면 삽입할 위치가 결정된것
     #return tNode를 해줘야함! 
     #내려가면서 tNode변경 맨 마지막에 단말노드에서 새로 생성해주는 것  
     #Llink, Rlink관계만 맨 끝에서 결정되느 tNode는 다시 그대로 반환됨
     #따라서 전체 트리의 루트는 변화가 없다.
    
    #[삽입 비재귀 용법]
    def InsertBST(self)->None:
        def _insertBST(root,data)->DNode:
            pParent=None 
            tNode=root 
            while tNode: #탐색실패가 목표 tNode는 self.__root임
                pParent=tNode
                if data==tNode.data: 
                    print('이미 같은 키가 있습니다.')
                    return root 
                elif data<tNode.data: tNode=tNode.Llink
                elif data>tNode.data: tNode=tNode.Rlink
            
            if pParent==None:root=DNode(data) #첫번째로 삽입된 경우는 위의 while문 들어가지도 않음

            # while문 빠져나온 시점에서 tNode에는 None값이 들어가이씅ㅁ
            #pParent에 노드를 저장해놨었음 
            elif data<pParent.data:pParent.Llink=DNode(data)
            elif data>pParent.data:pParent.Rlink=DNode(data)
            return root 

        print("\n이진 검색 트리: 데이터 삽입")
        while True: 
            num=int(input('임의의 정수입력(종료: 0) '))
            if num==0:break
            self.__root=_insertBST(self.__root,num)
            #삽입 삭제 시 루트노드의 주소값이 바뀐다.


    #[삭제] 삭제안에 삽입도 들어있는 셈이다. 

    def delte(self,data): #삭제할 위치를 결정!! 
        self.__root=self.__deleteBST(self.__root,data)

    def __deleteBST(self,tNode,data)->DNode:
        if (tNode==None): #트리가 비어있는 경우 None값 리턴 
            return None

        elif (data==tNode.data): #일치하는 데이터를 찾은 경우>
            tNode=self.__deleteNode(tNode)#deleteNode함수 실행해서 노드를 삭제
            #deleteNode함수 보면 실제로 삭제라기 보다는 데이터 및 Llink Rlink수정작업임
        
        #크기 비교하면서 data계속 탐색(재귀호출) 
        elif(data<tNode.data):
            tNode.Llink=self.__deleteBST(tNode.Llink, data)
        else:
            tNode.Rlink=self.__deleteBST(tNode.Rlink,data)   
        return tNode
    
    #아래의 함수는 삭제할 노드의 위치가 결정된 후에 링크의 연결작업을 
    #어떻게 해줄지에 대한 함수이다. 
    #__deleteBST의 if elif data==tNode.data일때
    # tNOde=self.__deteNode(tNode)를 호출한다. 
    
    def __deleteNode(self,tNode)->DNode: #삭제할 노드의 위치를 받고 
        #해당 노드의 자식이 몇개인지 검사한다. 

        #case1. 단말노드일 경우( 리프노드)
        if tNode.Llink==None and tNode.Rlink==None:
            return None #그냥 끊어주면 된다. 
        #case2. 자식이 하나만
        # Rlink만 있는 경우
        elif tNode.Llink==None: 
            return tNode.Rlink
        #Llink만 있는 경우 
        elif tNode.Rlink==None:
            return tNode.Llink
        #case3. 자식이 둘다! > 둘의 크기비교를 해주어야 한다. 
        else:
            #이 한줄동안 계속 재귀호출하면서 최종 (최소값, Rlink로 연결시킬노드)가 결정된다
            (rtnItem,rtnNode)=self.__deleteMinItem(tNode.Rlink)
            

            tNode.data=rtnItem #삭제하기로 했던 tNode의 data와 
            tNode.Rlink=rtnNode #Rlink를 재정의 해주면서 물리적인 삭제라기 보다는 재정의
            return tNode #그렇게 수정된 tNode를 넘겨준다. 
        
    #후계자는 왼쪽서브트리의 min넣어도 되고 우측 서브트리의 max넣어도 된다.
    def __deleteMinItem(self, tNode)->tuple: #Right subtree의 min값을 찾는다.
        if tNode.Llink==None: # Rlink의 왼쪽 자식이 없다면
            return (tNode.data ,tNode.Rlink)  #그게 min값이다. min데이터를 넘겨주고
        #tNode.Rlink는 min값의Rlink를 
        else:
            (rtnItem, rtnNode)=self.__deleteMinItem(tNode.Llink)
            tNode.Llink=rtnNode
            return (rtnItem,tNode)
    
    
    def DeleteBST(self)->None:
        #데이터 삭제 비재귀적용법
        def _deleteBST(root,data)->DNode:
            if not root:
                print('\n 키를 찾지 못했습니다.')
                return tNode 
            
            pParent=None #삭제할 노드의 부모노드
            tNode=root  #삭제할 노드 

            while data!=tNode.data: 
                pParnet=tNode
                if data<tNode.data:tNode=tNode.Llink
                elif data>tNode.data: tNode=tNode.RLlink

            if tNode.Llink==None and tNode.Rlink==None:
                if pParent==None:root=None  #이미 비어있다면 None 
                elif pParent!=None: #pParent의 Llink가 있는 것이면 Llink삭제
                    if pParent.Llink==tNode: pParnet.Llink=None
                    else: pParent.Rlink=None

            elif tNode.Llink==None or tNode.Rlink==None:
                if tNode.Llink!=None: pChild=tNode.Llink
                else: pChild=tNode.Rlink
                
                #루트노드만 한개있던 것을 삭제하는 경우 pParent는 None값임
                if pParent==None:root=pChild 
                #그 외 
                else: 
                    if pParent.Llink==tNode: pParent.Llink=pChild
                    else: pParent.Rlink=pChild
                
            else: #자식노드 2개일 경우 (tNode는 삭제할 노드임)
                sParent=tNode
                sNode=tNode.Llink
                while sNode.Rlink!=None: # 왼쪽 서브트리 최대값 찾기
                    sParent=sNode
                    sNode=sNode.Rlink

                if sParent.Llink==sNode: #삭제할 노드의 왼쪽 서브트리가 한개노드로만 구성된경우
                    #sParent=tNode인 상황이고 sParent의 Llink가 곧 sNode이다. 
                    sParent.Llink=sNode.Llink
                else: 
                    sParent.Rlink=sNode.Llink  #sNode는 왼쪽 서브트리의 맨 우측 단말노드일것
                    #얘는 맨 위로 갈 것임. 따라서 sNode는 사라질 것이고 sParent와 sNode의 Llink를 연결시켜주는 것이 맞음!!!  


                tNode.data=sNode.data #tNode는 데이터만 변경시켜주면됨
                tNode=sNode #sNode를 삭제해야한다. 
            del tNode
            return root
        
'''
[tNode = sNode:] 중요 %%%%%%%%%%%%%%%%%5 
이 라인은 tNode라는 변수를 sNode로 업데이트합니다. 
이는 실제로 tNode가 아닌 sNode를 삭제하기 위한 준비 단계입니다. 
여기서 주의할 점은 tNode가 더 이상 원래의 삭제할 노드를 가리키지 않게 되었다는 것입니다.

[del tNode:]

del tNode는 이제 sNode를 가리키고 있는 tNode 변수를 삭제합니다.
 이는 메모리에서 sNode를 제거하는 것입니다.
   tNode의 데이터는 이미 sNode의 데이터로 대체되었기 때문에, 
   이제 sNode를 안전하게 제거할 수 있습니다.
[return root:]

함수는 수정된 트리의 루트 노드를 반환합니다. 
이는 전체 트리 구조에 대한 참조를 유지하는 데 중요합니다.'''
        
        print('\n이진 검색트리: 데이터 삭제')
        while True:
            num=int(input('임의의 정수 입력(종료: 0)'))
            if num==0: break
            self.__root=_deleteBST(self.__root,num)


# from LinkedBSTree import *
if __name__ == '__main__':
    bst = LinkedBSTree()
    while (True):
        print('\n##### 이진 검색 트리 ###')
        print('1) 데이터 삽입')
        print('2) 데이터 삭제')
        print('3) 데이터 검색')
        print('4) 전체 출력')
        print('5) 프로그램 종료\n')
        print('메뉴 선택 : ', end=' ')
        choice = int(input())

        if choice == 1 :	bst.InsertBST()
        elif choice == 2 :	bst.DeleteBST()
        elif choice == 3 :	bst.SearchBST()
        elif choice == 4 :	bst.printBSTAll()
        elif choice == 5 :
            print('프로그램 종료... \n')
            break
        else: print('잘못 선택 하셨습니다. \n')



    
