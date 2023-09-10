a=list(map(int, input().split()))
n=int(input("찾고자 하는 숫자를 알려주세요 : "))
for i in range(len(a)):
    if a[i]==n:
        print(i)
        break
    elif n not in a:
        print(-1)
        break
