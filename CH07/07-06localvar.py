def addone():
    '''함수에서 대입에 사용되는 변순ㄴ 지역 변수'''
    i = 30
    i += 1
    print('\t지역 변수 i:', i) # 지역 변수 참조

i = 20 # 전역 변수
print('i:', i)
addone()
print('i:',i)
