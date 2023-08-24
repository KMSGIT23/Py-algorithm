n=int(input())
a=[]
s=0; d=0
for i in range(n):
    q=int(input())
    a.append(q)
    if a[i]>s:
        s=q
        d=i

print(d)
