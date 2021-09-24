color = dict(검은색='black', 흰색='white', 초록색='green', 파란색='blue')
print(color)

#항목 조회
print(color.get('초록색'))
print(color.get('노란색'))

#항목 추가
color['노란색'] = 'yellow'
print(color)
print()

#항목 삭제
c = '흰색'
print('삭제: %s %s' % (c, color.pop('흰색')))
print(color)
c = '빨간색'
print('삭제: %s %s' % (c, color.pop(c, '없는 색상')))

print('임의 삭제: {} '.format(color.popitem()))
print('임의 삭제 후: {} '.format(color))

c = '분홍색'
color[c] = 'pink'
del color[c]
print('{} 삭제 후: {}'.format(c, color))

color.clear()
print(color)
