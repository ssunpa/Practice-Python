year = int(input('윤년을 검사할 연도 입력 >> '))
print('입력한 년도 %d' % year)
cond1 = year % 4 == 0
cond2 = year % 100 != 0
cond3 = year % 400 == 0
result = cond1 and cond2 or cond3
print('개별 검사 {} and {} or {} : {}'.format(cond1, cond2, cond3, result))
print('통합 검사 : %s' % result)
