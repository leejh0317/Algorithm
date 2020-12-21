# 1046 : [기초-산술연산] 정수 3개 입력받아 합과 평균 출력하기
a, b, c = map(int, input().split())

# 합
print(a+b+c)
# 평균
print('%.1f' %((a+b+c)/3))