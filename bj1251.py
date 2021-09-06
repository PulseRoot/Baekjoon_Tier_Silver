# 알파벳 소문자로 이루어진 단어를 가지고 아래와 같은 과정을 해 보려고 한다.
# 먼저 단어에서 임의의 두 부분을 골라서 단어를 쪼갠다. 
# 즉, 주어진 단어를 세 개의 더 작은 단어로 나누는 것이다. 
# 각각은 적어도 길이가 1 이상인 단어여야 한다. 
# 이제 이렇게 나눈 세 개의 작은 단어들을 앞뒤를 뒤집고, 이를 다시 원래의 순서대로 합친다.
# 예를 들어,
# 단어 : arrested
# 세 단어로 나누기 : ar / rest / ed
# 각각 뒤집기 : ra / tser / de
# 합치기 : ratserde
# 단어가 주어지면, 
# 이렇게 만들 수 있는 단어 중에서 사전순으로 가장 앞서는 단어를 출력하는 프로그램을 작성하시오.
from random import *

word = str(input())
length = len(word)

#랜덤 숫자 생성
i1 = randint(0, length-2)
i2 = randint(i1, length-1)
i3 = randint(i2, length)

word1 = word[:i1] #문자열 나누기
word2 = word[i1:i2]
word3 = word[i2:length]

print(word1, word2, word3)

word1 = word1[::-1] # 문자열 뒤집기
word2 = word2[::-1]
word3 = word3[::-1]

word = word1 + word2 + word3 #문자열 합치기
print(word)