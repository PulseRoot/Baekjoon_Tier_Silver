#첫째 줄에 N의 진짜 약수의 개수가 주어진다. 이 개수는 50보다 작거나 같은 자연수이다. 
#둘째 줄에는 N의 진짜 약수가 주어진다. 
#1,000,000보다 작거나 같고, 2보다 크거나 같은 자연수이고, 중복되지 않는다.

print("진짜 약수의 개수를 입력하세요.")
num = int(input())
ary = [0] * 50
ary_copy  = [0] * 50

for i in range(0, num):
   print( str(i+1) +"번째 진짜 약수를 입력하세요.") 
   innum = int(input())
   ary[i] = innum

two = [0] * num
three = [0] * num
five = [0] * num

for i in range(0, num):
    ary_copy[i] = ary[i]

for i in range(0, num):
    while ary[i]%5 == 0:
        ary[i] = ary[i]/5
        five[i] = five[i] + 1
    while ary[i]%3 == 0:
        ary[i] = ary[i]/3
        three[i] = three[i] + 1
    while ary[i]%2 == 0:
        ary[i] = ary[i]/2
        two[i] = two[i] + 1        
                
total = (2 ** max(two)) * (3 ** max(three)) * (5 ** max(five))               

for i in range(0, num):
    if ary_copy[i] == total:
        total = total * 2

print("Answer : " + str(total))        