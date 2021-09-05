lis=[]
ran=int(input('enter range'))
active = True
while active:
    for i in range(ran):
        nm=int(input("please enter your number:"))
        
        lis.append(nm)
    for i in range(len(lis)):
        if lis[i]<lis[i+1]:
            pass
        elif lis[i]>lis[i+1]:
            lis=lis.sort
            print('list was not sorted sorting it now...')
            print(lis)
            
            active = False
            
    print("list was sorted"+lis)
        

            
