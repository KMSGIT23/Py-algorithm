def f(n, f, e, a):
    if n==1:
        print(f, "->", e)
        return
    f(n-1, f, a, e)
    print(f,"->", e)
    f(n-1, a, e, f)

