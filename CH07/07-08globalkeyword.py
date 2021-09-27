def addone():
    '''명시적으로 변수를 전역 변수로 지정'''
    global i # i를 명시적으로 전역 변수로 인식
    print('\t 전역 변수 i 읽기, i + 1:', i+1)
    i += 1

i = 20 # 전역 변수
print('i = ', i)
addone()
print('i = ', i)
