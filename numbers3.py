n=int(input("Enter the number"))
for i in range(1,n+1):
    print(' '*(n-1),end='')
    for j in range(1,i+1):
        print(j,end='')
    for m in range(i-1,0,-1):
        print(m,end='')
    print()    
    
    
        
