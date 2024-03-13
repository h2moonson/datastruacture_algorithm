class GNode: 
    def __init__(self,vertex:int, weight=0): #여기서 vertex는 column임!!
        #이미 __adjSList[row]에서 출발지점은 결정된 상태 
        self.vertex=vertex
        self.weight=weight
        self.link=None

class GraphType:
    def __init__(self, vertex: int): #정점의 개수를 받는다.
        self.__vertex=vertex
        self.__adjSList=[None for x in range(vertex)]#리스트를 생성한다.
        #None이지만 생성된 것 자체로 노드를 개념적으로 만들었다고 보면 됨 
        #@@ 이때 __adjSList 인덱스는 row로 생각하면 된다. 
        #insertedge에서 row 기준으로 인접노드와 연결이있는지 유무 확인후에 GNode(col,weight)로 추가한다.

    def insertEdge(self, row:int, col:int ,weight:int):
        if row>=self.__vertex or col>=self.__vertex:
            #print('그래프에 없는 정점입니다')
            return
        if self.__adjSList[row]==None: 
            self.__adjSList[row]=GNode(col,weight)#여기서 새로운 GNode가 생성된다.(간선이 생성됨)  else: #이미 있는 경우는 간선을 추가해준다.
        else:
            rNode=self.__adjSList[row]
            while rNode.link: #맨 마지막 원소까지 연결
                rNode=rNode.link
            #null까지 갔다면
            rNode.link=GNode(col,weight)

    def printAdjSList(self):
        for i in range(self.__vertex):
            print(f'\t정점 {chr(i+65)}의 인접 리스트: ',end='')
            tNode=self.__adjSList[i] #0번째- A에 연결된 애들을 다 출력해야함
            while tNode :
                print(f'{chr(tNode.vertex+65)}->',end=' ')
                tNode=tNode.link
            print('NULL')


    def DFSAdjSList(self, start_vertex: int):
        visited = [False for _ in range(self.__vertex)]
        #vertex에는 전체 노드 개수 
        #backtracking 방식, 방문여부를 마킹을 한다. 
        # 스택 생성
        S = []
        S.append(start_vertex)#방문한 노드를 스택에 추가하고 
        visited[start_vertex] = True #visited 스택에는 true로 바꿔준다

        while S:
            v = S.pop() #꺼낸애로 탐색 시작
            w = self.__adjSList[v]
            while w: #전체 탐색중인 노드 
                #adjSList[0]=A인데 A에 B, C가 연결된 그래프다?
                #[0]에는 삽입된 순서로 B->C->None의 연결리스트가 들어가있음
                #따라서 w.vertex를 하면 B가 나옴
                #B는 방문 안헀기에 스택에 추가하고 True로 변경 
                #이제 A는 중단하고B에대해 탐색. w=adjSList[w.vertex]
                #vertex자체가 정수형으로 인덱스로 정점을가리키기에 정점이 곧 인덱스 역할
                #visied에 넣는 것이 맞다.

                if not visited[w.vertex]: #adjSList에서 인접한 노드 자체를 가리킴 
                          #방문안한 인접 정점에 대해 수행
                    S.append(w.vertex)#스택에 추가하고 
                    visited[w.vertex] = True# 정점 방문 
                    print(f'{chr(w.verted+ 65)}', end=' ')
                    w = self.__adjSList[w.vertex]  
                else:
                    w = w.link #그림참고> A에서 B갔는데 B의 인접리스트는 B->A->D순임
                    #A는 이미 방문. w.link실행 D로 된다. 

            print('')
            #NULL이 되면 나오고 pop

    '''
    else: w = w.link: 이 코드는 현재 정점의 인접 리스트에서 다음 노드로
      이동하는 과정입니다. 만약 현재 정점 v에서 인접한 정점 w가 이미 방문된
        상태라면, 
    
    w.link를 통해 v의 다음 인접 정점으로 넘어갑니다. 
    이는 단순히 인접 리스트를 순회하는 것이지, 이전 분기점으로 
    돌아가는 백트래킹은 아닙니다.

    백트래킹의 올바른 구현
    스택을 사용한 DFS에서 백트래킹은 스택에서 원소를 꺼내는 과정(S.pop())에
      해당합니다. 스택의 맨 위에 있는 정점을 꺼내어 그 정점의 인접 정점을 
      탐색합니다. 만약 더 이상 탐색할 인접 정점이 없다면, 스택에서 다음
     정점을 꺼내어 탐색을 계속합니다. 이렇게 스택에서 원소를 꺼내는 
     과정이 실제로 백트래킹에 해당합니다.
    따라서 else: w = w.link는 백트래킹 과정이 아니라 인접 리스트 내에서의 
    순회 과정으로 이해하는 것이 적절합니다. 
    백트래킹은 스택을 사용하여 이전 정점으로 돌아가는 과정에서 발생합니다.
    '''
    def BFSAdjSList(self,start_vertex:int):
        visited=[False for x in range(self.__vertex)]
        Q=[]
        Q.append(start_vertex)
        visited[start_vertex]=True
        print(f'{chr(start_vertex+65)}', end=' ')

        v=start_vertex
        while Q:
            v=Q.pop(0)
            w=self.__adjSList[v] #GNode인스턴스
            while (w):
                if not visited[w.vertex]: #인접 노드 
                    Q.append(w.vertex)
                    visited[w.vertex]=True
                    print(f'{chr(w.vertex+65)}',end=' ')

                w=w.link #모든 레벨을 처리해야한다. @ 


       
        
    def __del__(self):
        for i in range(len(self.__adjSList)): #리스트 길이만큼 반복한다.
            temp=self.__adjSList[i] #순차적으로 처리 헤더 방문
            while temp:
                self.__adjSList[i]=temp.link #그 다음 노드로 연결 
                del temp
                temp=self.__adjSList[i]
        del self
'''
먼저, i=0에 대한 인접 리스트의 첫 번째 노드(temp = self.__adjSList[0])를 가져옵니다.

temp가 None이 아닐 때까지, 즉 인접 리스트에 노드가 남아있는 동안 반복합니다.

현재 temp가 가리키는 GNode 인스턴스(예: GNode(1))를 메모리에서 해제하기 전에, temp.link를 사용하여 다음 GNode 인스턴스로 temp를 업데이트합니다. 이렇게 하면 temp가 다음 노드를 가리키게 됩니다.

이제 현재 temp (예: GNode(1))를 메모리에서 해제합니다.

temp를 업데이트한 후, 다시 temp가 None이 될 때까지 2-4단계를 반복합니다. 이 과정은 리스트의 모든 노드를 메모리에서 해제할 때까지 계속됩니다.

모든 GNode 인스턴스가 메모리에서 해제된 후, del self를 통해 GraphType 객체 자체도 메모리에서 해제합니다.
                
'''