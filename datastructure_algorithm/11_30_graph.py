'''
그래프: G는 집합(Set) 두개로 구성 - 정점(Vertex 또는 Node) 간선(Edge)
인접(Adjacent)과 부속(Incident)
A,B가 연결되어 있을때 두 정점이 인접되어있다고 하고
간선(A,B)는 부속되어 있다고 한다. 
노드 B에 A가 진입하고 B에서 C,D로 진출하는 경우
B의 진입차수는 1이고 진출차수는 2이다. 전체 차수는 3이다. 

그래프를 만들고 정점을 빠짐없이 방문하는 순회(깊이우선순회stack-back tracking 너비우선순회queue 인접되어있는 모든 정점들을 방문 )
어디서 출발해서 어떻게 방문할 것인가? 수업때는 A에서 시작하고 오름차순으로 하겠지만 B,C ...에서 출발할수도 

<깊이 우선순회- back tracking 방식> 

방문했는지 안했는지 마킹을 한다. 
방문했으면 stack 에 push 1넣고 2 까지 push 2인접(1은 이미 방문, 방문안한 정점 3을 찾아감) 
visited[]에 true false여부로 넣어둠 
A   B  C  D  E  F  G  H
[1][2][3][4][5][6][7][8]
 t  t  f  f  f  f  f  f  << visited 

 5까지 갔을 때는 2, 3, 4이미 다 방문함
 5는 더이상 방문할 필요 x 5는 pop해버림
 4도 pop, 3도 pop, 2까지 와서는 6을 방문 
(back tracking...)

<너비 우선순회>  더 간단하다
visited배열과 queue
u에 인접한 모든 인접리스트 방문
1을 큐에 삽입. f-> t
1pop 2, 3, ,4 방문, 
2pop해서 인접한 애 조사, 다 했음
3pop해서 아직 방문 안한 5 삽입
4pop해서 6, 7 삽입
 
슬라이드 수정:G에서 DEF순으로 방문해야함 

'''
'''
	그래프 표현(인접 행렬): 알고리즘 구현
		파일명: GraphAdjMatrix.py
			- main	: 그래프 생성 및 간선 추가
			- 클래스	: GraphType
				그래프 생성 : __init__
				그래프 간선 추가 : insertEdge
				그래프 전체 출력 : printAdjMatrix
'''
# GNode class
class GNode :
    def __init__(self, vertex: int, weight = 0) :
        self.vertex = vertex    # 정점
        self.weight = weight    # 차수
        self.link = None

# GraphType class
class GraphType :
    def __init__(self, vertex: int) :
        self.__vertex = vertex                              # 정점의 개수  
        self.__adjSList = [ None for x in range(vertex) ]   # 인접 리스트
    
    def __del__(self):
        for i in range(len(self.__adjSList)) :
            temp = self.__adjSList[i]
            while temp :
                self.__adjSList[i] = temp.link
                del temp
                temp = self.__adjSList[i]
        del self
    #그래프 순회 (DFS)
    def DFSAdjSList(self, start_vertex: int ): #root를 받을 것임0 
        #각 정점의 방문 여부
        visited=[False for x in range(self.__vertex)] #전체 개수만큼 생성

        #스택을 생성해야함!!
        S=[]
        S.append(start_vertex)
        visited[start_vertex]=True 
        print(f'{chr(start_vertex+65)}', end=' ') #A의 아스키 코드 값이 65 그 다음 B, C,D순이니깐 ..

        v=start_vertex
        while S:
            w=self.__adjSList[v] 
            while w: #인접 정점있는 동안
                #방문안한 인접정점에 대해 수행
                if not visited[w.vertex]: #GNode인스턴스 현재 탐색중인 노드의 인접노드 자체
                    S.append(w.vertex)
                    visited[w.vertex]=True #정점 방문 
                    print(f'{chr(w.vertex+65)}', end=' ')
                    v=w.vertex
                    w=self.__adjSList[w.vertex]
                else: w=w.link 
                #방문안한 인접 정점이 없으면 스택 pop
                v=S.pop()
            print('')     

    
    #그래프순회 (BFS)
    def BFSAdjSList(self,vertex: int ): 
            visited=[False for x in range(vertex)] #
            Q=[]
            Q.append(vertex)
            visited[vertex]=True
            print(f'{chr(vertex+65)}', end=' ')

            v=vertex
            while Q:
                v=Q.pop(0)
                w=self.__adjSList[v]
                while (w):
                    if not visited[w.vertex]:
                        Q.append(w.vertex)
                        visited[w.vertex]=True
                        print(f'{chr(w.vertex+65)}', end=' ')

                    w=w.link


        
    

    # 그래프 간선 추가
    def insertEdge(self, row:int, col:int, weight:int) :
        if row >= self.__vertex or col >= self.__vertex :
            # print('그래프에 없는 정점입니다!!!')
            return
        if self.__adjSList[row] == None : 
            self.__adjSList[row] = GNode(col, weight)
        else :
            rNode = self.__adjSList[row]
            while rNode.link :
                rNode = rNode.link
            rNode.link = GNode(col, weight)

    # 그래프 전체 출력
    def printAdjSList(self) :
        for i in range(self.__vertex) :
            print(f'\t정점 {chr(i+65)}의 인접 리스트: ', end='')
            tNode = self.__adjSList[i]
            while tNode :
                print(f'{chr(tNode.vertex + 65)} -> ', end='')
                tNode = tNode.link
            print(' NULL')

if __name__ == '__main__' :
    # G9 : 무향 그래프 32슬라이드 그림 참고 
    G9 = GraphType(7)

    # 정점: A(0)
    G9.insertEdge(0, 1, 0)    # A(0) - B(1)
    G9.insertEdge(0, 2, 0)    # A(0) - C(2)
   
    # 정점: B(1)
    G9.insertEdge(1, 0, 0)    # B(1) - A(0)
    G9.insertEdge(1, 3, 0)    # B(1) - D(3)
    G9.insertEdge(1, 4, 0)    # B(1) - E(4)

    # 정점: C(2)
    G9.insertEdge(2, 0, 0)    # C(2) - A(0)
    G9.insertEdge(2, 4, 0)    # C(2) - E(4)

    # 정점: D(3)
    G9.insertEdge(3, 1, 0)    # D(3) - B(6)
    G9.insertEdge(3, 6, 0)    # D(3) - G(6)

    G9.insertEdge(4,1,0)
    G9.insertEdge(4,2,0)
    G9.insertEdge(4,6,0)

    G9.insertEdge(5,6,0)

    G9.insertEdge(6,3,0)
    G9.insertEdge(6,4,0)
    G9.insertEdge(6,5,0)
    G9.printAdjSList()
    G9.BFSAdjSList(0)
    G9.DFSAdjSList(0)