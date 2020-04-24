



class businessCard():
        
    def inits(self,name,email,addr):
        self.name = name
        self.dmail = email
        self.addr = addr


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
            
                
