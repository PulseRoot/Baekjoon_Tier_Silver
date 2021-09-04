print("구간 정수 갯수 입력 :")
num = int(input())
arr = [0] * (num + 1)

for i in range(0, num):
    print(str(i+1) + "번째 정수 입력")
    su = int(input())
    arr[i] = su  
print("n을 입력하세요.")
n = int(input()) 

cnt = 0
for i in range(0, num): 
    if(arr[i] == n):  
        cnt = 0
        print(str(cnt)) 
        break
    elif((arr[i] < n) & (arr[i+1] > n)):   
        for j in range(arr[i]+1, arr[i+1]): #9~12
           if j < n:
               cnt = cnt + arr[i+1] - n
               continue
           elif j == n:
               cnt = cnt + arr[i+1]-1 -n
               break 
        break              

print(str(cnt)) 

#입력 1과 2는 맞는데 4번
#8개 : 3 7 12 18 25 100 33 1000
#n = 59일때 답이 1065인데 1393나옴 ㅠㅠ