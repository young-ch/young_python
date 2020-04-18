print(">>>>>>반복문 >>>>>>>>")
test = [1,2,3,4,5]

for i in test:
    print(i)

test1 = [(1,2),(3,4),(5,6)]
for(i,j) in test1:
    print("sum :" , i+j)

for i in range(0,10) :
    print(i)

print(">>>>>>Lambda>>>>>>>>")
multiply_number = lambda x: x*1500
print(multiply_number(5))

print(">>>>>>file I/O 출력>>>>>>>")
f = open("filename.txt","w")
f.write("이 문자열은 파일에 기록됩니다.\n")
f.write("문자만 기록되나요??")
f.close()

r = open("young_program.py", 'r')
data = r.read()
print(data)
r.close()

print(">>>>>>오류처리>>>>>>>")
try:
    num = 10/1
    print(num)
except Exception:
    print("0으로 나눌 수 없습니다.")
finally:
    print("무조건 실행시키기")
