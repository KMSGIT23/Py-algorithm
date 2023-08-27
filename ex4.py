a=[]
n=int(input("학생 수를 입력하세요 : "))
for i in range(n):
    q=input()
    a.append(q)

s=set()
for j in range(n):
    s.add(a[j])
if a[j] in s:
    print(a[j])
