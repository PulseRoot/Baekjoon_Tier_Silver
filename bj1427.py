# 배열을 정렬하는 것은 쉽다. 수가 주어지면, 그 수의 각 자리수를 내림차순으로 정렬해보자.

N = str(input())
List = []
for i in range(0, len(N)):
    List.append(N[i])

Answer = ""

List.sort(reverse = True)

for i in range(0, len(N)):
     Answer = Answer + List[i]

print(Answer)



