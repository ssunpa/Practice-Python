# 평균 평점 3.8 이상이면 장학금 지급 대상자

grade = float(input('1학기 평균 평점은? '))
if 3.8 <= grade:
    print('장학금 지급 대상자입니다.')
print('당신의 평균 평점 : %.1f' % grade)
