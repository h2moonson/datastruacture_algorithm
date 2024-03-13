#큐의 이해 
'''
	큐: 알고리즘 구현 -- 단순연결리스트
		파일명: LinkedQueue.py
			- 큐의 생성.소멸자  :  __init__, __del__
			- 데이터 삽입.삭제  : push, pop     # enQueue, deQueue
			- 데이터 확인(peek) : front, back   # peek
			- 빈 스택 여부 판단 : empty
			- 큐의 크기         : size
			- 큐의 전체 원소 출력: printQueue
'''
class LinkedQueue:
    class SNode:
        def __init__(self, data,link=None):
            self.data=data
            self.link=link
    def __init__(self):
        self.__front=None
        self.__rear=None
        self.__count=0

    def __del__(self):
        temp=self.__front 
        while temp:
            self.__front=temp.link #삭제하기 전에 미리 두번째 노드 가리키도록
            del temp 
            temp=self.__front
        self.__count=0 #다 지우면 0이지
        del self #이 라인은 역할이 뭐지? 


    def push(self,data)->None:
        nNode=self.SNode(data,None)
        if not self.__front: #첫번째 push라면
            self.__front=nNode #front가 nNode 가리키도록

        else: 
            self.__rear.link=nNode #기존 rear가 새로운 노드 link
        #****self.__rear는 첫번째 push 던지 아니던지 상관없다!
        self.__rear=nNode #rear 최신으로 업데이트 
        self.__count+=1 #count변수 업데이트

    def pop(self):
        if not self.__front: #비어있다면
            return None  #None반환
        else: 
            temp=self.__front #소멸자 때와 비슷
            self.__front=temp.link
            del temp
            self.__count-=1

    def front(self): #첫번째 원소 확인
        if self.__front==None:
            return None
        return self.__front.data
    def back(self):
        if self.__rear==None:
            return None
        return self.__rear.data

    def empty(self)->bool:
        return self.__front==None #front값이 있는지 없는지로 공백 판단
    
    def size(self):
        return self.__count
    
    def printQueue(self):
        temp=self.__front
        print('\n QUEUE [',end='')
        while temp:
            print(temp.data, end='')
            temp=temp.link
        print(']\n')

if __name__=='__main__':
    Q=LinkedQueue()
    while(True):
        print('\n### 큐 구현: 단순 연결 리스트 ###')
        print('1) 데이터 삽입(push, enQueue)')
        print('2) 데이터 삭제(pop, deQueue)')
        print('3) 전체 출력')
        print('4) 프로그램 종료')
        choice = int(input('메뉴 선택: '))
        if choice==1: num=int(input('삽입할 데이터: ')); Q.push(num)
        elif choice==2: print(f'삭제 된 데이터: {Q.front()}'); Q.pop()
        elif choice==3: Q.printQueue()
        elif choice==4: print('프로그램 종료... ');break
        else: print('잘못선택하셨습니다.')


