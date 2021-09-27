def sumvalue(value, **kwargs):
    hap = value
    for key in kwargs:
        hap += kwargs[key]
    return hap

coffeeprice = {'에스프레소':3000, '아메리카노':5000, '카페라테':6000}
print(sumvalue(1000, **coffeeprice))
print(sumvalue(value = 2000, **coffeeprice))
print(sumvalue(**coffeeprice, value = 2000)) # 둘 다 키워드 인자
