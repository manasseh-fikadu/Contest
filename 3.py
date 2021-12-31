def patternGenerator(n) -> None:
    for i in range(2):
        print()
        for j in range(n):
            print("#"*(n-1)+" ",end='')

i = int(input("Enter N: "))
print(patternGenerator(i))
