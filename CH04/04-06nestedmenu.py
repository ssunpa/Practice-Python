category = int(input('원하는 음료는? 1. 커피 2. 주스 : '))

if category == 1:
    menu = int(input('번호선택 1. 아메리카노 2. 카페라테 3. 카푸치노 : '))
    if menu == 1:
        print('1.아메리카노 선택')
    elif menu == 2:
        print('2.카페라테 선택')
    else:
        print('3.카푸치노 선택')
else:
    menu = int(input('번호선택 1. 키위주스 2. 오렌지주스 3. 자몽주스 : '))
    if menu == 1:
        print('1.키위주스 선택')
    elif menu == 2:
        print('2.오렌지주스 선택')
    else:
        print('3.자몽주스 선택')



    
