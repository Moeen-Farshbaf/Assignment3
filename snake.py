n = int(input("length of snake?: "))


for i in range(n):
    if i%2 == 0:
        print("*", end='')
        
    elif i % 2 == 1:
        print("#", end='')