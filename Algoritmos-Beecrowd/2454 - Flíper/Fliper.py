x = input().split()
p, r = x
p = int(p)
r = int(r)

if(p == 0):
    print("C")
elif(p == 1 and r == 0):
    print("B")
elif(p == 1 and r == 1):
    print("A")