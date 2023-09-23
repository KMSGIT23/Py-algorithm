def ins_sort(a):
    n = len(a)
    for i in range(1, n): #1부터 n-1까지
        key = a[i] #i번 위치에 있는 값을 key에 저장
        #f를 i바로 왼쪽 위치로 저장
        j = i - 1
        # 리스트의 i번 위치에 있는 값과 key를 비교해 key가 삽입될 적절한 위치를 찾음
        while j >= 0 and a[j] > key:
            a[j + 1] = a[j] #삽입할 공간이 생기도록 값을 오른쪽으로 한 칸 이동
            j-=1
        a[j + 1] = key #찾은 삽입 위치에 key를 저장

if __name__ == "__main__":
    d = list(map(int, input().split()))
    ins_sort(d)
    print(d)
