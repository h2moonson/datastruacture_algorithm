'''
첫째 줄에 괄호열을 나타내는 문자열(스트링)이 주어짐. 길이는 1이상 30이하
첫째 줄에 그 괄호열의 값을 나타내는 정수 출력
입력이 올바르지 못하면 반드시 0을 출력 

올바른 입력 조건: (,),[,] 네개의 기호가 올바르게 들어와야함 
쌍이 맞아야하고 x가 올바른 괄호열이면 (x)나 [x]도 올바른 괄호열
x,y모두 올바른 괄호열이면 xy도 올바른 괄호열이다.
(()[[]])올바른 괄호열, ([)]나 (()()[]는 올바르지 못한 예

정의: 
1. ()=2
2. []=3
3.(x)는 2x값(x)
4.[x]는 3x값(x) 로 계산 
5. 올바른 괄호열 X, Y가 결합된 XY의 괄호값 r값(XY)=값(X)+값(Y)

예를 들어 (()[[]])([])의 값은 (2+3x3) 2x3 = 2x11 +2x3=28이다.

(()[[]])([])=28
[][]((])=0
'''

'''
# 메모. 파이썬 빈 리스트 판단 : 
파이썬은 if문에서 empty list는 False를, empty가 아닌 list는 True를 리턴합니다.
따라서, 다음과 같이 간단히 if not list 또는 if list처럼 empty를 확인할 수 있습니다. 
'''
def bracket_operation(bracket):
    if (len(bracket)%2==1): #괄호개수가 홀수면 오류 
        print('개수가 올바르지 않습니다.')
        return 0
    S=[]
    tmp=1
    answer=0
    #괄호를 열면 그냥 append하고 쌍이 맞는 닫는 괄호오면 쌍이 맞는 열린 괄호 찾고 그에 맞는 숫자를 곱한다고 생각하면 복잡하다.
    #(()[])()를 생각하면  스택에 (23이 되고 숫자있으면 2+3은 더해주지만 )들어오면 그 숫자를 또 곱해야 하는..복잡한 상황 
    #( 들어오는 순간 tmp변수에 2를 곱해주고 [ 들어오면 3을 곱해주는 식으로 생각하자
    #(()의 경우 2*2가 오고 )가 왔기에 answer에 2*2를 넘겨준다. 
    # (()에서 닫힌애는 stack에서 제거 ( 만 남고 tmp에 2를 나눠서 update
    # []가 들어올 경우는 2가 곱해져 있는 상태에서 3을 곱해서 6이 되고 answer에 넘겨줌
    # 최종적으로 2(2+3)이 자동으로 구현되는 셈이다.
    for i in range (len(bracket)):
        if bracket[i]=='(':
            S.append(bracket[i])
            tmp*=2

        elif bracket[i]=='[':
            S.append(bracket[i])
            tmp*=3
        elif bracket[i]==')':
            if not S or S[-1]=='[': #스택이 비어있는 경우에 닫는 괄호가 들어오면 안되지..
                return 0
            if bracket[i-1]=='(': # *주의*바로 이전 인덱스의 원소와 짝이 맞을 때만 answer에 더해줌. 그게 아닐 경우 전체를 감싸는 큰 괄호일것 !!
                #(()[]에서 )를 검사하는 과정> answer에는 이미 2*2+2*3이 들어가있음 )왔다고 2*2를 더해주면 안됨! 
                answer+=tmp
            S.pop()
            tmp=tmp//2 #괄호 쌍이 완성됐기에 제거해줌
        else: 
            if not S or S[-1]=='(':
                return 0
            if bracket[i-1]=="[":
                answer+=tmp
            S.pop()
            tmp=tmp//3
    if S: #이상한 기호가 입력되었을 경우 스택에 무엇인가 남아있을 것 
         print('잘못된 기호가 입력되었습니다.')
         return 0
    else: 
        return answer
 
if __name__=='__main__':
    #input_str=input('괄호 식을 입력하세요: ')
    input_list=list(input('괄호식을 입력하세요: '))
    #리스트로 받아서 인덱스로 관리하는게 더 편하다. 
    print(f'결과는 {bracket_operation(input_list)} 입니다.')

    

    
    
