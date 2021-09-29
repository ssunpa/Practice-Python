from random import choice
#한글의 format 출력 문제로 '보'를 '보오'로 표기
dcs = {'가위':'보오', '바위':'가위', '보오':'바'}
#출력에 필요한 단어를 구성해 리스트로 생성
tit = ['비김', '철수', '영희', '승자']
rsp = ('가위', '바위', '보오')
#제목출력
print('*'*17)
print('{:4} {:4} {:4}'.format(tit[1], tit[2], tit[3]))
print('*'*17)

for _ in range(10):
    #철수의 결정
    cs = choice(rsp)
    #영희의 결정
    yh = choice(rsp)

    #철수와 영희희 결정 출력
    print('{:4} {:4}'.format(cs, yh), end =' ')

    #비기는 조건
    if cs == yh:
        index = 0 #비김 출력
    #철수가 이기는 조건
    elif dcs[cs] == yh:
        index = 1
    #영희가 이기는 조건
    else:
        index = 2
    #게임 결과 출력
    print('{:4}'.format(tit[index]))
