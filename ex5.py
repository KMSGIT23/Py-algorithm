def f(n, i=1, sum=1):
    if i < n:
        i += 1
        sum = sum * i
        return f(n, i, sum)
    else:
        return sum

if __name__ == "__main__":
    n = int(input())
    print(f(n))
