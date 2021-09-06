# 표준 입력한 실수와 연산식의 산술 연산 및 결과 출력

num1 = float(input('첫 번째 수 입력 >> '))
num2 = float(input('두 번째 수 입력 >> '))
print('합:', num1 + num2)
print('차:', num1 - num2)
print('곱하기:', num1 * num2)
print('나누기:', num1 / num2)
expression = input('연산식 입력 >> ')
print('연산식:', expression)
print('결과:', eval(expression))
