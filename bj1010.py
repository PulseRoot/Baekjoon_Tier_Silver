import math

print("테스트 횟수를 입력하시오. : ")
text = int(input())

for i in range(0, text):
    print("서쪽 다리의 갯수 입력 : ")
    west = int(input())
    print("동쪽 다리의 갯수 입력 : ")
    east = int(input())
    if(east < west):
        while east < west :
            print("서쪽 다리의 갯수인 "+west+"개보다 높은 수로 입력하세요.")
            east = int(input())
    answer = math.factorial(east) / (math.factorial(west) * math.factorial(east - west))
    print("경우의 수는 " + str(int(answer)) + "\n")

