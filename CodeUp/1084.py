# 1084 : [기초-종합] 빛 섞어 색 만들기(설명)
a, b, c = map(int, input().split())
cnt = 0

for i in range(a):
    for j in range(b):
        for k in range(c):
            print('{} {} {}'.format(i, j, k))
            # print(f'{i} {j} {k}') python 3.6 이상
            cnt += 1
print(cnt)