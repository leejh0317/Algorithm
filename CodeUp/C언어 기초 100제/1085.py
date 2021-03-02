# 1085 : [기초-종합] 소리 파일 저장용량 계산하기(설명)
h, b, c, s = map(int, input().split())
bit = h*b*c*s/8
mb = bit/(1024*1024)
print('%.1f' %mb, 'MB')