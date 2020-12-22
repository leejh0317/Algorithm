# 1086 : [기초-종합] 그림 파일 저장용량 계산하기(설명)
w, h, b = map(int, input().split())
bit = w*h*b/8
mb = bit/(1024*1024)
print('%.2f' %mb, 'MB')