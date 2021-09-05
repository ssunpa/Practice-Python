# 지구와 달까지의 거리를 만 단위로 출력

distance = 384400
unit = 10000
manUnit, remainder = divmod(distance, unit)
print('지구에서 달까지의 거리:' ,manUnit, '만', remainder, '킬로미터') 
