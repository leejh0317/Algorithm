# 1076 : [기초-반복실행구조] 문자 1개 입력받아 알파벳 출력하기(설명)
c = ord(input())

for x in range(97, c+1):
    print(chr(x))