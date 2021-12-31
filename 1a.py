#Pattern 1

n = 5
for i in range(1, n+1):
    for j in range(n-i+1):
        print(" ", end = '')
    for k in range(2*i -1):
        print("*", end = '')
    print("")
   
#Pattern 2
n = 4
for i in range(1, n+ 1):
    for j in range(i):
        print("*", end = "")
    print("")
