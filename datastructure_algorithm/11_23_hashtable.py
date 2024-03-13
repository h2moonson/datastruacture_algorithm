'''
해시테이블 
키를 균등하게 분포? 
해시함수에서 키 값을 계산 

가장 보편적으로 쓰는 방법 > 나눠서 쓰는 방법 
곱하기 방법도 있고 여러가지 방법이 있음 

prob? 충돌이 발생되지 않는 위치로 넣어야함 


<개방형주소방식>

선형조사- 소스코드보고 쉽게 따라할 수 있을 것 
이차원조사
이중해싱-보조해싱함수 사용

prob? 군집화 발생 > 충돌이 발생했을 때, 그 다음다음 하다보면 군집화

27pg 충돌이 발생 이웃된 빈 공간을 찾아간다. 

------
선형조사 알고리즘에서 삽입 삭제 검색을 할고 할떄 

search- index값 있으면 반환
없으면, 즉 같은 애가 들어있으면 

삭제 시 none값으로 주면 안됨. 있었는데 없어진 것인지 아니면 원래 없었던 것인지 모름
22위치를 none으로 했다면 그 다음ㅇ위치를 찾으러 가지 않는 문제가 발생할 수 있다. 


-----
이차조사: 더 먼곳으로 삽입 +1^2 2차 충돌 +2^2 .. 이런식으로 군집화 최소화
이중해싱: 고도 해싱 함수를 추가적으로 제시

-----
<폐쇄주소방식>
Chaining 연결리스트의 헤더노드를 참조한다.
비어있을떄 그냥 node생성해서 연결
비어있지 않는다면 새로운 노드 생성시킨 것을 맨 마지막 노드를 찾아서 새로운 노드를 연결 
그림 12-4참조 ,
결국 단순연결 리스트에서 key값만 추가된 것 0~12= key값 > 각각의 key에 노드를 물리고 물린다. 
'''
#해시함수 선형조사, 이차조사 주석하면서 결과값 비교해볼 것 

class HashOpenAddressing: 
    def __init__(self, n:int):
        self.__table = [None for i in range(n)] #크기 받고 None으로 원소 생성
        self.__count = 0 #삽입 삭제하면서 원소 개수 업데이트
        self.__DELETED = -54321 #삭제시키면 이를 표시할 상수

    # 해시 함수
    def __Hash(self, i:int, num):
        #return (num + i) % len(self.__table)        # 선형 조사
        return (num + i*i) % len(self.__table)    # 이차 조사

    # 데이터 삽입
    def insert(self, num):
        if self.__count < len(self.__table): #자리가 비어있는지 확인 
            for i in range(len(self.__table)):
                slot = self.__Hash(i, num) #중복된 경우는 i값이 변하면서 다음위치를 찾아서 삽입됨
                #아래 if 문이 실행되어야 삽입이 되어 return 을 함 
                if self.__table[slot] == None or self.__table[slot] == self.__DELETED:
                    self.__table[slot] = num
                    self.__count += 1
                    return num
        return None
        # if self.__count == len(self.__table):

    # 데이터 삭제
    def delete(self, num):
        for i in range(len(self.__table)):
            slot = self.__Hash(i, num)
            if self.__table[slot] == None: #삭제하려는 데이터가 없는 경우 
                return None
            elif self.__table[slot] == num: #핵심!! None객체값을 넘겨주면 안된다. 
                self.__table[slot] = self.__DELETED
                self.__count -= 1
                return num
        return None

    # 데이터 검색
    # NOT_FOUND = -12345  # constant
    def search(self, num):
        for i in range(len(self.__table)):
            slot = self.__Hash(i, num)
            if self.__table[slot] == None:     #none값이면 없는것      
                return None
                # return HashOpenAddressed.NOT_FOUND
            if self.__table[slot] == num: 
                return self.__table[slot]
                # return slot    # Found at self.__table[slot]
        return None
        # return self.__NOT_FOUND
    
    # 전체 원소 출력
    def output(self):
        print(f'count({self.__count}): {self.__table}')

class Chaining:
    class SNode:
        def __init__(self,data):
            self.data=data
            self.link=None
    def __init__(self,n:int):
        self.__table=[None]*n
    def _Hash(self,num):
        return num%len(self.__table)
    def insert(self,num):
        slot=self._Hash(num)
        if self.__table[slot] is None:
            self.__table[slot]=self.SNode(num)
        else: 
            tNode=self.__table[slot]
            while tNode.link:
                tNode=tNode.link
            tNode.link=self.SNode(num)
        return
    def delete(self,num): # 94 3 42 55 에서 3을 지우고 94와 42를 연결해야함 
        targetslot=self.__Hash(num)
        tNode=self.__table[targetslot]
        if tNode is None:
            return None
        pre=None #직전 데이터 값을 저장하고 있어야함 94값을 알아야!!
        while tNode and tNode.data!=num: 
            pre=tNode
            tNode=tNode.link
        if pre is None: #1개짜리 삭제를 할 경우
            self.__table[targetslot]=tNode.link
        else:
            pre.link=tNode.link
        data=tNode.data
        del tNode
        return data 

    def search(self,num):
        slot=self.__Hash(num)
        tNode=self.__table[slot]
        while tNode:
            if tNode.data==num:
                break
            tNode=tNode.link
        if tNode: return tNode.data
        return None
    def output(self):
        for i in range(len(self.__table)):
            print(f'{i:3}', end=' ') 
            tNode=self.__table[i]
            while tNode:
                print(f'-->{tNode.data}',end=' ')
                tNode=tNode.link
            print('')

# from HashOpenAddressing import *
if __name__ == '__main__':       
    #h = HashOpenAddressing(13)-->개방형 주소방식으로 사용할 경우 주석 해제
    h=Chaining(13) #-->폐쇄 주소 방식
    while (True):
        print('\n ### 해시 테이블 ###')
        print('1) 데이터 삽입')
        print('2) 데이터 삭제')
        print('3) 데이터 검색')
        print('4) 전체 출력')
        print('5) 프로그램 종료\n')
        print('메뉴 선택 : ', end=' ')
        choice = int(input())

        if choice == 1:
            num = int(input('삽입 할 데이터 입력: '))
            inserted = h.insert(num)
            if inserted: print(f'삽입 된 데이터: {inserted}')
            else: print(f'데이터 삽입에 실패하였습니다.')
        elif choice == 2:
            num = int(input('삭제 할 데이터 입력: '))
            deleted = h.delete(num)
            if deleted: print(f'삭제 된 데이터: {deleted}')
            else: print(f'데이터가 존재하지 않습니다.')
        elif choice == 3:
            num = int(input('검색 할 데이터 입력: '))
            searched = h.search(num)
            if searched: print(f'검색된 데이터: {searched}')
            else: print(f'데이터가 존재하지 않습니다.')
        elif choice == 4: h.output()
        elif choice == 5:
            print('프로그램 종료!!!')
            break
        else: print('잘못 선택 하셨습니다.')