'''
정답예제: 
print를 10다 찍어서 빈 값은 None으로 출력하도록 구현했음
front rear를 -1로 두고 시작함 
'''
# front 삭제할 데이터의 위치(가장처음 들어온 값)
# rear 삽입할 데이터의 위치 
# rear값을 size로 나눠준 값이 front와 같아지면 포화상태이거나 아예 비었거나 > count변수 활용해서 
class CircularQueue:
    def __init__(self, capacity):
        self.__data=[None]*capacity
        self.__front=0
        self.__rear=0
        self.__count=0
        self.__capacity=capacity

    def push(self,item)->None: #포화상태인지 먼저 판단
        if not self.full():  
            self.__data[self.__rear]=item #삽입할 위치에 그대로 삽입
            self.__rear=(self.__rear+1)%self.__capacity #rear값을 +1해줌  
            self.__count+=1
        else: print('꽉 찬 큐입니다.')
    def pop(self)->None:
        if not self.empty(): #비어있는지 판단
            #temp=self.__front%self.__capacity #삭제할 기존의 front위치 저장 *수정 1 : main함수 부분에서 self.__front를 찍고 pop실행하기에 굳이 이렇게 할 필요x
            self.__front=(self.__front+1)%self.__capacity #그 다음 인덱스를 가리키도록 함(실질적인 삭제는x 참조를 해제할뿐) 
            # 실질적인 삭제는 원형큐가 한바퀴돌아서 새로운 값으로 변경될때 이루어진다고 보면 됨 
            self.__count-=1
            # return self.__data[temp]  *수정 1: main함수 부분에서 self.__front를 찍고 pop실행하기에 굳이 이렇게 할 필요x 
        else: print('이미 빈 큐입니다. 삭제 진행 불가 ')
    def front(self): #첫번째로 삽입된 데이터 확인
        if not self.empty():
            return self.__data[self.__front]
    def back(self):#마지막으로 삽입된 데이터 확인 
        if not self.empty(): 
            return self.__data[self.__rear]
    def size(self)->int:
        return self.__count 
    def empty(self)->bool: #front와 rear로 공백 여부 판단 
        return self.__front==self.__rear and self.__count==0
    def full(self)->bool: #꽉 찬 경우 판단은 rear+1을 하고 size로 나눠서 비교 
        return self.__front==self.__rear and self.__count!=0
    def printQueue(self)->None: 
        if not self.empty():
            for i in range (self.size()):
                print(f'{self.__data[(self.__front+i)%self.__capacity]} ', end=' ')
        else: print('비어있는 큐입니다. \n')

#Q=CircularQueue(10)


if __name__=='__main__':
    print('###큐 구현: 리스트 ###')
    print('''1) 데이터 삽입: (enQueue) \n2) 데이터 삭제: (deQueue)\n3) 전체 출력\n4) 프로그램 종료''')
    cir_queue=CircularQueue(5)
    choice=0
    while (choice!=4): 
        choice=int(input('메뉴선택 : '))
    
        if choice ==1 : 
            data=int(input('입력할 데이터: '))
            cir_queue.push(data)
        elif choice ==2 : 
            print(f'삭제한 데이터:{cir_queue.front()}')
            cir_queue.pop()
        elif choice ==3 : 
            print('전체 출력: ',end=' ')
            cir_queue.printQueue()
        elif choice ==4 : 
            print('프로그램 종료합니다. ')
            break
    