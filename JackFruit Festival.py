x=list(map(int,input().split()))
n=x[0]
d=x[1]
arr=list(map(int,input().split()))
arr.sort()
print(sum(arr[-d:]))
