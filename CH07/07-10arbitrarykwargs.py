def mykeyprint(**kwargs):
    for key in kwargs:
        print('{}: {} '.format(key, kwargs[key]), end=' ')
    print()

mykeyprint(여자친구=6, 마마무=4)
mykeyprint(방탄소년단=7, 블랙핑크=4, 트와이스=9)

coffeeprice = {'에소프레소':3000, '아메리카노':5000, '카페라테':6000}
mycar = {'brand': '현대', 'model':'제네시스', 'year':2020}
mykeyprint(**coffeeprice)
mykeyprint(**mycar)
