class ListStack:
    def __init__(self):
        self.__data=[]
        self.__top=None 
    def push(self,num)->None:
        self.__data.append(num)
        self.__top=self.__data[-1] #수정5. 추가하면 업데이트 해줘야
    def pop(self)->None:
        if not self.empty():
            self.__data.pop()
            if len(self.__data)==0: #수정 8. 마지막 하나를 pop한 경우는 empty이용하면 top이 업데이트가 안된 상태이므로 x
                self.__top=None
            else: self.__top=self.__data[-1] #수정 7. pop하고서도 top변수 수정해라
        else: 
            print('이미 비어있습니다.')#수정3. 비어있는 경우 pop x

    def top(self): #수정4. self.__top 초기값 None
        if self.__top==None: #비어있다면 
           return None
        return self.__top
    
    def size(self)->int:
        return len(self.__data)
    def empty(self)->bool:
        return self.top() is None #수정1. top으로 판단 > 사실 그냥 len으로 하면 편한데...
    def printQueue(self)->None:#수정2. 스택이 비어있을 경우 생각
        if self.top()!=None: 
            for i in range (len(self.__data)):
                print(f'{self.__data[i]}',end=' ')
            print(" ")
        else: print('빈 스택입니다.') 


if __name__=='__main__':
    print('###스택 구현: 1차원 배열 ###')
    print('''1) 데이터 삽입: PUSH \n2) 데이터 삭제: POP\n3) 전체 출력\n4) 프로그램 종료''')
    teststack=ListStack()
    choice=0
    while (choice!=4): 
        choice=int(input('메뉴선택 : '))
    
        if choice ==1 : 
            data=int(input('입력할 데이터: '))
            teststack.push(data)
        elif choice ==2 : 
            print(f'삭제한 데이터:{teststack.top()}')
            teststack.pop() #수정6. top으로 출력하고 pop으로 제거해줘라
        elif choice ==3 : 
            print('전체 출력: ',end=' ')
            teststack.printQueue()#수정7. print문 안에 리턴값없는 함수 넣으면 None 이 찍힘!!
        elif choice ==4 : 
            print('프로그램 종료합니다. ')
            break
    



    
