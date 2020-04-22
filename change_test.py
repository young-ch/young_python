#재귀함수 n! = 1*2*n

def factorial(n):
    
    r = 1
    i = 2
    
    for i in range(1,n+1):
        
        r *= i
          
    return r

print(factorial(10))

