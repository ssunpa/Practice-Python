# 표준 입력한 수를 여러 진수로 출력

base = int(input('입력할 정수의 진수(base)는? '))
invar = input(str(base) + '진수 정수 입력 >> ')
data = int(invar, base)

print('2진수:', bin(data))
print('8진수:', oct(data))
print('10진수:', int(data))
print('16진수:', hex(data))
