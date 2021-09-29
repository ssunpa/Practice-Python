#K-pop 가수와 곡을 차트 순위에 맞춰 입력
singer = ['방탄소년단', '디핵', '에스파', '방탄소년단']
song = ['My Universe', 'OHAYO MY NIGHT', 'Next Level', 'Permission to Dance']

#zip()함수로 가수와 곡을 조합
kpop = list(zip(singer, song))
print(kpop)

#dic()와 enumeratezip() 함수로 순위를 키로 가수와 곡을 사전으로 구성
kpchart = dict(enumerate(kpop, start = 1))

#일반 출력
print(kpchart)
print()

#모듈 pprint의 pprint() 함수 활용
import pprint
pprint.pprint(kpchart)
