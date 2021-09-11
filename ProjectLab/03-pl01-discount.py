'''
10,000원 이상 ~ 20,000원 미만 -> 1% 할인
20,000원 이상 ~ 40,000원 미만 -> 2% 할인
4,000원 이상 -> 4% 할인
총 가격을 입력받아 원 가격, 할인된 가격, 할인율, 할인액을 출력하기
'''

price = int(input('총 가격(원 가격) 입력 >> '))

rate1 = (10000 <= price < 20000) * (1/100)
rate2 = (20000 <= price < 40000) * (2/100)
rate3 = (40000 <= price) * (4/100)
rate = rate1 + rate2 + rate3

discount = price * rate
discPrice = price - discount
print('원 가격:', price, '할인된 가격:', discPrice)
print('할인율:', rate, '할인액:',discount) 
