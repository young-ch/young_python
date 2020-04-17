print("hollow")

x = [0,1,4]
y = ["yellow","mongkey"]

if 4 in x: print("정답")

z = {
    "name" : "영철",
    "age" : 20,
    0 : "hellow"
    }

print(z["name"])
print(z["age"])


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
