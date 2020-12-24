# 1092 : [기초-종합] 함께 문제 푸는 날(설명)
a, b, c = map(int, input().split())
day = 1

while True:
    if day % a != 0 or day % b != 0 or day % c != 0:
        day += 1
    elif day % a == 0 and day % b == 0 and day % c == 0:
        break
print(day)