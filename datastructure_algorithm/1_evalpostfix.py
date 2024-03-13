'''
스택 활용: 후위 표기법을 이용한 수식 계산
- evalPostfix		: 후위 표기법으로 수식 계산
- InfixToPostfix	: 중위 표기법을 후위 표기법으로 변환
중위 표기(Infix): (A + B) - C
후위 표기(Postfix): A B + C -
전위 표기(Prefix): - + A B C 
'''
#연산자 여부를 판별 > 괄호는 여기에 해당되지 않음 
def isOperator(op:str)->bool:
    return op=='+'or op=='-' or op=='*'or op=='/'
    #이 넷중에 있으면 return 1 아니면 0

#연산자 우선순위를 사전설정(수치로)
def precedence(op:str)->int:
    if op=='(': return 0
    elif op=='+' or op=='-': return 1
    elif op=='*' or op=='/': return 2
    else: return 3

def InfixToPostfix(infix:str)->str:
    #S는 스택으로사용, postfix는 print문이라고 생각하고 코드 작성 
    S=[] 
    #split으로 구분할 것이므로 앞 뒤 공백 생성> replace함수 이용 변환 
    infix=infix.replace('(', ' ( ')
    infix=infix.replace(')', ' ) ') 
    infix=infix.replace('+', ' + ')
    infix = infix.replace('-', ' - ')
    infix = infix.replace('*', ' * ')
    infix = infix.replace('/', ' / ')
    infix = infix.split() #마지막에 공백문자로 다 분리시켜버림

    postfix=[]
    for st in infix:
        #1) 여는 괄호는 push
        if st== '(':
            S.append(st) 
         # 2) ')'를 만나면 '('가 나올 때까지 pop 한 후에 '('는 버린다.
        elif st==')':
            while S[-1]!='(':
                postfix.append(S[-1]) #출력할 애들 postfix에다가 넣는다
                S.pop() #미리 복사본 만들어 놓고 pop시켜야함! 
            S.pop() #마지막 여는 괄호 pop
        #3)연산자인 경우 우선순위 비교 
        elif isOperator(st):
            while len(S) and precedence(S[-1])>=precedence(st):
                #while len(S)조건있어야 연산자 처음 넣을 때 비교 안하고 넣음 
                #자신보다 우선순위 높은 애는 pop
                postfix.append(S[-1])
                S.pop()
            S.append(st) #자기보다 낮은 우선순위 만나면 자기자신push
            #혹은 위의 while문이 종료되고 나서 자기자신 push 

        #4)피연산자(숫자) 인 경우는 그냥 push
        elif str.isdigit(st): # 문자열의 구성요소가 모두 숫자인지 확인
            #123같은 경우 얘는 문자열인지 숫자인지 인식 못한다.
                       
        # str.isdigit("문자열")
        # "문자열".isdigit() 2가지 방식이 있다
            postfix.append(st)
        elif st==' ': continue #빈칸이라면 pass

        else: 
            print('잘못된 수식!!!')
            return
    #스택에 남은 연산자 모두 pop한다. 마지막 점검 과정? 
    while len(S):
        postfix.append(S[-1]) 
        S.pop()
    return postfix # 결국 반환하는 건 postfix라는 후위표기로 변환된 리스트! 

def evalPostfix(postfix:str)->int:
    S=[] #S에는 숫자만 넣는다 연산자가 들어오는 순간 2개 꺼내서 비교한다! 
    #이미 후위 표기로 변환된 식을 받았다. operand는 그냥 push 하고 
    #operator를 받으면 2개 pop해서 operator로 계산하면 된다.
    for st in postfix:
        
        if str.isdigit(st):  #operand(숫자)라면 그냥append
            S.append(st)
        elif isOperator(st): #연산자가 왔다면 
            op2=int(S[-1]); S.pop()
            op1=int(S[-1]); S.pop()
         #계산결과는 다시 append해준다.
            if st == '+': S.append(op1 + op2)
            elif st == '-': S.append(op1 - op2)
            elif st == '*': S.append(op1 * op2)
            elif st == '/': S.append(op1 / op2)
            elif st == ' ' : continue
            else:
                print('잘못된 수식!!!')
                return
    if len(S):
        res=S[-1] #다 계산하고 하나 남아있는게 결과값이다.
        S.pop()
    return res #res 리턴안해주면 none값 찍힌다.. 

if __name__=='__main__':
    infix=input('수식입력:')
    postfix=InfixToPostfix(infix)
    print(f'후위표기법 변환: {postfix}')

    res=evalPostfix(postfix)
    print(f'연산결과는: {res}')