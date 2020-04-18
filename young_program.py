print(">>>>>>>>>>>>>>>>문자열 기본문법>>>>>>>>>>>>>>")

test = "young string"
test1 = 2
test = r'C:\Nature'

first = r'youngman'
last = "kim"

print(test)
print(test1)
print(first + last)
print(last * 5)

test_str = "goodman"

print(test_str[0])
print(test_str[-2])
print(test_str[1:5])
print(test_str[2:])

print(">>>>>>>>>>>>>>>>if 기본문법>>>>>>>>>>>>>>")
name = "teed"

if name in 'teeg':
    print("정답입니다")
elif name in 'teed':
    print("teed 입니다")
else : print("아무것도 아닙니다")

print(">>>>>>>>>> list ?>>>>>>>>>>")
b=[1,3,5]
c=['cash','monkey','test']
d = [7, 9, ['Myungseo', 'L3opold7'],['test','test22']]


print(b[-1])
print(c[-2])
print(d[-1][1])


def dsum(a, b):
    result = a + b
    return result 


print(">>>>>>>>>dsum함수>>>>>>>>>>")
print(dsum(2,3))

print(">>>>>>>>>chat>>>>>>>>>>")
def chat(name1, name2):
  print("%s : 안녕?" % name1)
  print("%s : 하이" % name2)


chat("영철","나경")
test = [1,2,3,4,5]
test[3] = 6

print(test)

print(">>>>>>>>>내장 함수>>>>>>>>>")

print(">>>append>>")
test = [1,2]
test.append(3)
print(test)

print(">>>del>>")
test = ['a','b','c','d','e']
del test[1:3]
print (test)

print(">>>>>>sort>>>>>>")
test = [3,1,2,5,4]
test1 = test
test.sort()
print(test)
test1.reverse()
print(test1)

print(">>>>>>>>>tuple>>>>>>>>>")
#tuple은 값을 변경할 수 없다.
tp1 = (1,2,3)
tp2 = (4,5,6)
print(tp1[2])
print(tp1[1:])
print(tp1 + tp2)
print(tp2 * 2)

print(">>>>>>dictionary>>>>>>>>>")
#키=값 형태로 이루어진 자료형입니다. 이렇게 대응 관계를 나타내는 자료형을 연관배열 또는 hash라고 합니다.

dic1 = dict()
dic2 = {'k1': 'v1', 'k2': 'v2', 'k3': 'v3'}
dic3 = dict([('name', 'L3opold7'), ('phone','01079972791')])
dic4 = dict(firstname='Myungseo', lastname='kang')
dic5 = {'ls':['a','b','c']}

print(dic2)               # {'k1': 'v1', 'k3': 'v3', 'k2': 'v2'}
print(dic2['k2'])         # v2
print(dic3)               # {'phone': '010-1234-5678', 'name': 'L3opold7'}
print(dic3['name'])       # L3opold7
print(dic4)               # {'firstname': 'Myungseo', 'lastname': 'Kang'}
print(dic4['firstname'])  # Myungseo
print(dic5['ls'])         # ['a', 'b', 'c']


test = {'name':'young', 'number':12, 3: 'test'}
#del test[3]
print(test)
#내용 모두 지우기
#test.clear()

print(test.keys())
print(test.values())
print(test.items())


















