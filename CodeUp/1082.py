# 1082 : [기초-종합] 16진수 구구단?
n = int(input(), 16)

for i in range(1, 16):
    x = i * n

    print('{}*{}={}'.format('%X' %n, '%X' %i, '%X' %x))