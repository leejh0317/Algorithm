# 1063 : [기초-삼항연산] 두 정수 입력받아 큰 수 출력하기(설명)
n, m = map(int, input().split())
c = n if n > m else m

print(c)