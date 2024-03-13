#후위 표기로 변환된 식으로 노드로 구성해준다.
for st in postfix:
    temp=DNode(st)=
    if isOperator(st): # d

S=[]
node=self.__root
while S or node: 
    if node:
        print(node.data, end=' ')
        S.append(node)
        node=node.Llink
    else:
        node=S.pop().Rlink

def Preorder(self):
    def_Preorder(tNode):
    if tNode:
        print(tNode.data,end=' ')
        _Preorder(tNode.Llink)
        _Preorder(tNode.Rlink)
    _Preorder(self.__root)
    