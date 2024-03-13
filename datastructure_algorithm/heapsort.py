#Heapify Algorithm : 특정한 하나의 노드에 대해서 수행 
'''
특정 노드의 두 자식 중에서 더 큰 자식과 자신의 위치를 바꾸는 알고리즘
위치를 바꾼 뒤에서 여전히 자식이 존재하는 경우 또 자식 중에서 더 큰 자식과
자신의 위치를 바꾸어야 함 > 자식이 
자식 노드가 없다면 시도할 필요 없음 

힙구조: 배열로 나타내면 된다
1. HeapSort 함수= 힙정렬 
 1) buildheap함수 -> 힙 구조를 먼저 생성해라
 2) 맨 마지막 원소와 root를 swap (원소 개수만큼 반복) (N)
  2-1) tree size를 축소시켜 가면서 계속해서 힙정렬> 맨 처음에는 9라면 그 다음에는 8... (-1)
     percolateDown 함수를 루트 노드에 대해 수행 (logN)
2. BuildHeap > 힙 구조 생성 > 시간복잡도 n/2 
 1) n/2만큼 만복하면서 percolateDown 수행 

3. percolateDown 함수 >재귀함수 !!
 1) 기준 root를 받아서 왼쪽 자식, 오르쪽 자식 비교 
 2) 비교 할때 child의 범위를 지정해줘야함 최대 array의 마지막인덱스까지만 - 재귀함수 탈출조건인셈 
 3) root보다 child가 크다면 
  3-1) SWAP을 한다.
  3-2) percolateDown함수 재귀호출4

4. SWAP함수 - temp변수 이용, 3줄이면 swap 구현 가능 

'''
def heapSort(SList):
    num=len(SList) #9번
    buildHeap(SList) 
    for i in range (len(SList)-1, 0,-1): #max 위치에 있는 것과 root를 교환 
        SWAP(SList,0, i) 
        percolateDown(SList,0,i-1) #root노드를 기준으로, i-1 size의 트리에서 다시 힙 구조 
    return SList     
def buildHeap(SList): #힙 생성 시간 복잡도 n/2
    num=len(SList) #9
    for i in range (num//2-1, -1,-1): # 3부터 0까지 4번 반복 > 0번부터 시작하는 인덱스 고려 
        percolateDown(SList,i, num-1) # 자식 노드와 비교 
    return SList
    

def percolateDown(SList, root:int, end: int):
        child=2*root+1
        right=2*root+2
        if child<=end: #5.말단 노드의 경우는 child> end가 될 테니 더 이상 비교 과정 수행되지 않음
            if right<=end and SList[child]<SList[right]: #1.child에는 둘 중 더 큰 원소의 인덱스 넣는다
                child=right #2.실제로 두 개를 swap하는 것은 아님 그냥 child변수에 더 큰애를 넣는다는 뜻
            if SList[root]<SList[child]: #3.부모노드보다 자식노드 두 개중 큰 값이 더 크면? swap해라 
                SWAP(SList,root,child)
                percolateDown(SList, child, end) #4.언제까지 재귀호출하는가? 
def SWAP(SList, i, j):
    temp = SList[i]
    SList[i] = SList[j]
    SList[j] = temp

import random
#sample_list=[5,2,3,9,6,1,8,4,7]
sample_list=[]


while(len(sample_list)!=8):
    num=random.randint(0,100)
    if num not in sample_list:
        sample_list.append(num)

print(f'정렬 전: {sample_list}')
print(f'buildHeap: {buildHeap(sample_list)}')
print(f'정렬 후:{heapSort(sample_list)} ')
