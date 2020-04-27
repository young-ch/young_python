#import stock
import os
import class_base


#현재경로 가져오기
os.getcwd()


#함수의 인자로 리스트를받은 후 리스트 내에 있는 모든 정숫값에 대한 최댓값과 최솟값을 반환하는 함수를 작성하세요.

#fh = class_base.businessCard()
#Ac = class_base()

#fh.get_max_min()

#cb = class_base.businessCard()
#cb.print_info('young','young90','korea_city')


#ac1 = Ac.Account("young1990")
#print(ac1.name)

cp = class_base.Point(12,56)


print(cp.get())
print(cp.move(12,43))

a = class_base.Stock()
a.market

f = open('buy_list.txt','rt')
lines = f.readlines()
f.close
for line in lines:
    print(line, end="")

d = open('sel_list.txt', 'wt')
d.write('삼성전자\n')
d.write('현대차\n')
d.close()

print("-------------------------------")

ct = class_base.txt_number()
ct.open_num()
