# 1067 : [기초-조건/선택실행구조] 정수 1개 입력받아 분석하기(설명)
n = input()

print('minus' if n[0] == '-' else 'plus')
print('even' if int(n) % 2 == 0 else 'odd')