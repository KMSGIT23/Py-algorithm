def f(a, b):
    i=min(a, b)
    while True:
        if a%i==0 and b%i==0:
            return i
        i-=1

if __name__=="__main__":
    a, b=map(int, input().split())
    print(f(a, b))
