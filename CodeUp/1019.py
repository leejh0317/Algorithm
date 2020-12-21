# 1019 : [기초-입출력] 연월일 입력받아 그대로 출력하기
yyyy, mm, dd = map(int, input().split('.'))

print('%04d.%02d.%02d' %(yyyy, mm, dd))