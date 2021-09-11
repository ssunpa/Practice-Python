MAXNUM = 4
MAXHEIGHT = 130

more = True
cnt = 0
while more:
    height = float(input('키는? '))
    if height < MAXHEIGHT:
        cnt += 1
        print('입장', '%d명' % cnt)
    else:
        print('입장 제한')
    if cnt == MAXNUM:
        more = False
else:
    print('%d명 모두 입장. 다음 번에 이용하세요.' %cnt)
