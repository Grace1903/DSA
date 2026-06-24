def maximini():
    arr=list(map(int,input().split()))
    k=int(input())
    arr.sort()
    print(arr[-k],arr[k-1])
maximini()
