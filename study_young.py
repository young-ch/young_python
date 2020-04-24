#import stock
import os
import class_base

#현재경로 가져오기
os.getcwd()


#함수의 인자로 리스트를받은 후 리스트 내에 있는 모든 정숫값에 대한 최댓값과 최솟값을 반환하는 함수를 작성하세요.

fh = class_base.businessCard()
fh.get_max_min()

cb = class_base.businessCard()
cb.print_info('young','young90','korea_city')
