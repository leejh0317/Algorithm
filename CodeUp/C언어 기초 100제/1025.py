# 1025 : [기초-입출력] 정수 1개 입력받아 나누어 출력하기(설명)
n = input()
i = 0

for _ in range(len(n)):
    print('[%d]' %int(n[i].ljust(len(n)-i,'0')))
    i+=1