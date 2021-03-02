# 1027 : [기초-입출력] 년월일 입력 받아 형식 바꿔 출력하기(설명)
yyyy, mm, dd = map(int, input().split('.'))

print('%02d-%02d-%04d' %(dd,mm,yyyy))

# print(f'{dd}-{mm}-{yyyy}') -> python 3.6 이상