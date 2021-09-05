# 행성 지구 반지름을 입력받아 지구 둘레 길이 구하기

planet = input('행성의 이름은? ')
strRadius = input(planet + ' 반지름은? ')
radius = int(strRadius)

length = 2 * 3.14 * radius
print(planet, '반지름:', radius)
print(planet, '둘레길이:', length)
