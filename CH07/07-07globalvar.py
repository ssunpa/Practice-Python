def addone():
    '''대입이 없는 변수가 참조되면 전역 변수로 인식'''
    print('\t 전역 변수 i 읽기, i + 1:', i + 1)

i = 20
print('i = ', i)
addone()
print('i = ', i)
