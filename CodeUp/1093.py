# 1093 : [기초-1차원배열] 이상한 출석 번호 부르기1(설명)
student = [0 for _ in range(23)]
n = int(input())
call = list(map(int, input().split()))

for i in range(n):
    student[call[i]-1] += 1
print(*student, end = ' ')