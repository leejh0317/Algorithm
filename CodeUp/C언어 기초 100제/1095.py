# 1095 : [기초-1차원배열] 이상한 출석 번호 부르기3(설명)
n = int(input())
call = list(map(int, input().split()))
call.sort()

print(call[0])