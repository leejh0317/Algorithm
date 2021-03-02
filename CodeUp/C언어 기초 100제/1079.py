# 1079 : [기초-종합] 원하는 문자가 입력될 때까지 반복 출력하기
c = input().split()

for x in c:
    print(x)
    
    if x == 'q':
        break