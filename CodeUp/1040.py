# 1040 : [기초-산술연산] 정수 1개 입력받아 부호 바꿔 출력하기(설명)
n = input()

if n[0] == '-':
    print(abs((int(n))))
else:
    n = '-'+n
    print(int(n))