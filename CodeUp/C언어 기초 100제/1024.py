# 1024 : [기초-입출력] 단어 1개 입력받아 나누어 출력하기(설명)
s = input()
idx = 0

for _ in range(len(s)):
    print("'%c'" %s[idx])
    idx+=1