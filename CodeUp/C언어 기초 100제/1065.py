# 1065 : [기초-조건/선택실행구조] 정수 3개 입력받아 짝수만 출력하기(설명)
x = input().split()

for i in range(len(x)):
    if int(x[i]) % 2 == 0:
        print(x[i])