
class Account:
        num_accounts = 0
        
        def __init__(self,name):
            self.name = name
            Account.num_accounts += 1

        def __del__(self):
            Account.num_accounts -= 1           
            
class Stock:
        market = "kospi"
        
class txt_number:
        def open_num(self):
                f = open("number_list.txt","wt")
                list_num = []
                for x in range(0,10,1):
                        list_num.append(x)
                        

                       
                f.write(str(list_num))

                f.close

                d = open("number_list.txt","rt")
                lines = d.readlines()
                print(lines)
                
class Point:

        def __init__(self,x,y):
                self.x = x
                self.y = y
                
        def setx(self, x):
                self.x = x     

        def sety(self, y):
                self.y = y

        def get(self):
                return(self.x, self.y)
        
        def move(self,dx,dy):
                self.x += dx
                self.y += dy

                return(self.x,self.y)
                
class businessCard():


    def print_info(self,name,email,addr):

        self.name = name
        self.email = email
        self.addr = addr
        
        print("------------------")
        print("Name: ", name)
        print("Email:", email)
        print("addr: ", addr)
        print("------------------")

            
        
    def get_max_min(self):
        list_num = []
        while True:
            num = input("숫자를 입력하세요: ")

            
            list_num.append(num)

            end = input()    
            if end == 'x':
                print("종료합니다.")
                break

        print(list_num)    
        min_num = min(list_num)
        max_num = max(list_num)
        
        print("가장 작은 숫자:", min_num)
        print("가장 큰 숫자:", max_num)
            
                
