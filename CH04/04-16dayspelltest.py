days = ['monday', 'tuesday', 'wednesday' ,'thursday', 'friday', 'saturday', 'sunday']

while True:
    user = input('영어로 요일을 입력 >> ')
    if user not in days:
        print('다시 입력해보기!')
        continue
    print('입력한 요일 %s, 정답입니다.' % user)
    break

print('종료'.center(15, '*'))
