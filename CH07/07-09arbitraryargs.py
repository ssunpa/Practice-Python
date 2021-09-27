def hello(*names):
    for each in names:
        print('안녕, {}!'.format(each))

hello('도라에몽')
hello('이슬이', '노진구', '비실이')
hello(*['퉁퉁이', '골목대장'])
