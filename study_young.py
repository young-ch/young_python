
i = 0
n = 0

for n in range(0,5):
    for i in range(0,n) :
        print("*", end='')
        i = i + 1
    print("\n")
    

line = 2

for x in range(1, line * 2, 2):
    print((" " * ( (line * 2 - 1 - x) // 2 )) + ("*" * x))

for y in range(line * 2-3, 0, -2):
    print((" " * ( (line * 2 - 1 - y) // 2 )) + "*" * y)
