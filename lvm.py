n=int(input())
l=[]
st=[]
reg=0
for i in range(n):
    x=list(input().split())
    l.append(x)
i=0
while i<n:
    if l[i][0]=='PUSH':
        st.append(int(l[i][1]))
        i+=1
    elif l[i][0]=='STORE':
        reg=int(st.pop())
        i+=1
    elif l[i][0]=='LOAD':
        st.append(reg)
        i+=1
    elif l[i][0]=='PLUS':
        n1=st.pop()
        n2=st.pop()
        st.append(n1+n2)
        i+=1
    elif l[i][0]=='TIMES':
        n1=st.pop()
        n2=st.pop()
        st.append(n1*n2)
        i+=1
    elif l[i][0]=='IFZERO':
        x=st.pop()
        if x==0:
            i=int(l[i][1])
        else:
            i+=1
    else:
        print(st[-1])
        break
    
        
