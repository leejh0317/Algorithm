# 1064 : [기초-삼항연산] 정수 3개 입력받아 가장 작은 수 출력하기(설명)
a, b, c = map(int, input().split())
x = a if a<b and a<c else b if b<a and b<c else c

print(x)