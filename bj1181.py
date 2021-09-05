# 알파벳 소문자로 이루어진 N개의 단어가 들어오면 
# 아래와 같은 조건에 따라 정렬하는 프로그램을 작성하시오.
# 길이가 짧은 것부터
# 길이가 같으면 사전 순으로

print("input words number ")
num = int(input())
arr = [""] * num

for i in range(0, num):
    arr[i] = str(input())

set_arr = set(arr) #중복제거
arr = list(set_arr) #다시 arr에 저장

arr.sort() #사전순
arr.sort(key=len) #길이순 정렬

for i in range(len(arr)):
    print(arr[i])         