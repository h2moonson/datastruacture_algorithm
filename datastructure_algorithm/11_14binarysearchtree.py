'''
이진검색트리의 개념: 트리의 구조에 따라 시간복잡도가 달라질 수 있다.
포화 이진 트리 같은 경우는 log(n)의 시간복잡도 이지만
편향이진트리가 발생할 경우는 최대 n의 시간복잡도를 지니게 될 수도 있다.

이진검색트리의 조건: 이진 탐색과 마찬가지로 모든 노드는 서로다른 키를 가져야 한다.(유일한 key값) 
그리고 각 노드는 최대 2개의 자식을 갖는다. 검색이 가능하려면 정렬이 되어있어야한다.
[왼쪽 서브트리 키값< 루트의 키값< 오른쪽 서브 트리의 키값 ]의 구조를 보인다.
-탐색: 크기 비교해서 ==일때 까지 타고간다.
-삽입: 검색실패가 결정된 위치 ppt10번에서 검색실패한 위치의 왼쪽 자식노드로 넣어준다. 4<5이므로 5의 왼쪽 자식노드 
 이때, temp에 담아서 내려가다가 Llink와 Rlink가 Null일 경우! 이때 부모노드 5의 주소값을 가지고 있어야한다.

-삭제: 삭제할 노드의 탐색 및 후계자 설정(그 자리에 어떤애를 넣을것인가) 
이때, 삭제한 노드의 자식노드가 1개라면 그냥 그 자식노드의 연결만 그대로 올려주면 된다. 구조가 깨지지x
자식노드가 2개라면 왼쪽 서브트리의 최대값을 가진 노드를 탐색하고, 오른쪽 서브트리에서 가장 작은 값을 탐색소로 선택할것인지 최대로 설정할 것인지
루트 기준 왼쪽 서브트리의 가장 큰값 Rlink, 우측 서브트리의 가장 작은 값 Llink> ppt에서는 왼쪽서브트리의 max인 5가 선정되어 올라감  
5자리 다시 또 자시노드가 채워줘야함

16pg 슈도 코드:
같으면 return T
다르면 좌우 비교 Llink 타거나 Rlink탄다
Null 이 됐을 때는 탐색 실패 

탐색 실패 시 newnode를  만든다.
이떄 T값 parent로 백업 시켜둠 
T의 Link

삭제하려는 노드의 
Llink나 Rlink가                      

>오늘 배운 모든 것 > 편향트리가 생성될 수 있음 
'''

class DNode :
    def __init__ (self, data, Llink=None, Rlink=None):
        self.data = data
        self.Llink = Llink
        self.Rlink = Rlink

class BSTree:
	def __init__(self):
		self.__root = None

	# 이진 검색 트리(BST): 데이터 검색> 재귀적용법으로 구현 
	def search(self, data) -> DNode:
		return self.__searchBST(self.__root, data)
	
	def __searchBST(self, tNode:DNode, data) -> DNode:
		if (tNode==None): return None
		elif (data==tNode.data) :return tNode
		elif (data<tNode.Llink): return self.__searchBST(tNode.Llink, data)
		else: return self.__searchBST(tNode.Rlink, data)
    
		
		

	# 이진 검색 트리(BST): 데이터 삽입 >재귀적용법으로 구현
	def insert(self, data):
		self.__root = self.__insertBST(self.__root, data)
	def __insertBST(self, tNode:DNode, data) -> DNode:
		if (tNode==None): 
			tNode=DNode(data,None,None)
		elif(data<tNode.data): 
			tNode.Llink=self.__insertBST(tNode.Llink, data)
		else:
			tNode.Rlink=self.__insertBST(tNode.Rlink,data)
		return tNode
	

	# 이진 탐색 트리(BST): 데이터 삭제
	def delete(self, data):
		self.__root = self.__deleteBST(self.__root, data)	
	def __deleteBST(self, tNode:DNode, data) -> DNode:
		if (tNode==None): 
			return None
		elif (data==tNode.data):
			tNode=self.__deleteNode(tNode)
		elif(data<tNode.data):
			tNode.Llink=self.__deleteBST(tNode.Llink,data)
		else:
			tNode.Rlink=self.__deleteBST(tNode.Rlink,data)
		return tNode

 #얘는 __deleteBST에서 삭제할 위치 찾고 노드의 연결을 끊는 함수  
	def __deleteNode(self, tNode:DNode) -> DNode:
		# 3가지 case
		#     1. tNode이 리프 노드
		#     2. tNode이 자식이 하나만 있음
		#     3. tNode이 자식이 둘 있음
		if tNode.Llink == None and tNode.Rlink == None:
			return None
		elif tNode.Llink == None:  # case 2(오른쪽 자식 뿐)
			return tNode.Rlink
		elif tNode.Rlink == None: # case 2(왼쪽 자식 뿐)
			return tNode.Llink
		else: # case 3(두 자식이 다 있음)
			(rtnItem, rtnNode) = self.__deleteMinItem(tNode.Rlink)
			tNode.data = rtnItem
			tNode.Rlink = rtnNode
			return tNode

	def __deleteMinItem(self, tNode:DNode) -> tuple:
		if tNode.Llink == None:
			return (tNode.data, tNode.Rlink)
		else:
			(rtnItem, rtnNode) = self.__deleteMinItem(tNode.Llink)
			tNode.Llink = rtnNode
			return (rtnItem, tNode)

	# 기타
	def isEmpty(self) -> bool:
		return self.__root == None

	def clear(self):
		self.__root = None

	def printBSTAll(self):
		def _Preorder(tNode):
			if tNode :
				print(tNode.data, end=' ')
				_Preorder(tNode.Llink)
				_Preorder(tNode.Rlink)
		_Preorder(self.__root)
 
# from BSTree import *
if __name__ == '__main__':
    bst = BSTree()

    bst.insert(10)
    bst.insert(20)
    bst.insert(5)
    bst.insert(80)
    bst.insert(90)
    bst.insert(7550)
    bst.insert(30)
    bst.insert(77)
    bst.insert(15)
    bst.insert(40)
    # bst.printBSTAll()

    bst.delete(7550)
    bst.delete(10)
    # bst.printBSTAll()