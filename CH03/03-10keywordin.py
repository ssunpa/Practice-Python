#멤버십 검사 in으로 배운 파이썬 키워드 검사

inkey = input('파이썬 키워드를 입력하세요 >> ')
keywords = "'False', 'True', and', 'in', 'is', 'not, 'or'"
print('입력단어 {}, 키워드인가? {}'.format(inkey, inkey in keywords))
