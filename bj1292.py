A, B = map(int, input().split())

arr = []

for i in range(1,46):
    arr += [i] * i
    #arr 본 리스트에 [i]라는 값을 i개 가진 리스트를 더한다.

print(sum(arr[A-1:B]))    