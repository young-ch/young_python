

def plu(a,b):
    sum1 = a + b
    
    return sum1 

def mul(a,b):
    mull = a * b
    
    return mull 

def minu(a,b):
    minu2 = a - b
    
    return minu2

def div(a,b):
    div1 = a / b
    
    return div1

try:
    while True:
        print("계산기 입니다. 숫자 2개를 입력하세요.\n")
        a = int(input('첫번째 숫자 : '))
        b = int(input('두번째 숫자 : '))
        temp = input('사칙연산 입력 : ')
        
        
        if temp == '+' :
            print(plu(a,b))
        elif temp == '-' :
            print(minu(a,b))
        elif temp == '*' :
            print(mul(a,b)) 
        else :
            print(div(a,b))

        print("끝내겠습니까?")
        end = input('끝내려면 x or X를 눌러주세요. :')
        print(end)
        if end == 'x' :
            break
        elif end == 'X' :
            break
        
        
except:
    print("오류발생")
