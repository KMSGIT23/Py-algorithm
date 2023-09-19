def fa(n, f, e, a):
    if n==1:
        print(f, "->", e)
        return
    fa(n-1, f, a, e)
    print(f,"->", e)
    fa(n-1, a, e, f)

