from time import localtime
hour = localtime().tm_hour
mnt = localtime().tm_min

if hour < 10:
    print('지금 시각 : %d시 %d분, 조조 할인 가능!' % (hour, mnt))
else:
    print('지금 시각 : %d시 %d분, 조조 할인 불가능!' % (hour, mnt))
