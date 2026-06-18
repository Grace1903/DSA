def maxmin():
    arr=list(map(int,input().split()))
    maxi=arr[0]
    mini=arr[0]
    for x in arr:
        if x>maxi:
            maxi=x
        if x<mini:
            mini=x
    print(maxi,mini)
maxmin()