#딕셔너리로 구현> 동빈나 예제
#key값에 데이터를 넣어서 반환 값을 Node class로 주는 형태 
class Node:
    def __init__(self,data,left_node, right_node):
        self.data=data
        self.left_data=left_node
        self.right_data=right_node

#전위 순회
def pre_order(node):
    print(node.data, end=' ') #자기 자신 먼저 출력
    if node.left_data!=None: #왼쪽 노드가 있다면
        pre_order(tree[node.left_node]) #tree
    if node.right_node!=None:
        pre_order(tree[node.right_node])
#중위 순회
def in_order(node):
    if node.left_data!=None: #왼쪽부터 탐색하고
        in_order(tree[node.left_node])
    print(node.data, end=' ') #자식이 없는 경우 자기 자신 출력
    if node.right_node!=None: #오른쪽 탐색>
        in_order(tree[node.right_node]) 
#후위 순회 
def post_order(node):
    if node.left_node!=None:
        post_order(tree[node.left_node])
    if node.right_node!=None:
        post_order(tree[node.right_node])
    print(node.data, end=' ')
n=int(input()) #7입력 2^k -1 개수로 맞춰라 
tree={}

for i in range (n):
    data, left_node, right_node=input().split() #입력 받음 A B C/ B D E/C F G입력해라 
    if left_node=='None':
        left_node=None
    if right_node=='None':
        right_node=None
    tree[data]=Node(data, left_node, right_node) #딕셔너리 형태로 구현>tree{[B: Node(A,B,C)], [D: Node(B, D,E)], [F: Node(C, F, G)]} 가 들어가 있게 된다
pre_order(tree['A'])
print()
in_order(tree['A'])
print()
post_order(tree['A'])
print()