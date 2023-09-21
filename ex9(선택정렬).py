def find_min(a):
    n=len(a)
    min_index=0
    for i in range(1, n):
        if a[i]<a[min_index]:
            min_index=i
    return min_index

def select_sort(a):
    result=[]
    while a: #리스트에 값이 남아 있는 동안 반복
        min_index=find_min(a) #리스트에 남아 있는 것중 최소값의 위치
        value=a.pop(min_index) #찾은 최솟값을 빼어내서 value에 저장
        result.append(value) #value를 결과 리스트에 순서대로 추가
    return result

if __name__=="__main__":
    a=list(map(int, input().split()))
    print(select_sort(a))
