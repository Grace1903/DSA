def movezeros():
    arr=list(map(int,input().split()))
    temp=[]
    for i in arr:
        if i!=0:
            temp.append(i)
    while len(temp)!=len(arr):
        temp.append(0)
    print(*temp)
movezeros()