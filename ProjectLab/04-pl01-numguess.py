import random
answer = random.randint(1, 10)

indata = int(input('1에서 10 사이의 정수 입력 >> '))
while True:
    if indata == answer:
        print('정답입니다!')
        break
    elif indata < answer:
        str = '{}보다 더 큰 수로 다시 입력 >> '.format(indata)
    else:
        str = '{}보다 더 작은 수로 다시 입력 >> '.format(indata)
    indata = int(input(str))

print(' 종료 '.center(30, '*'))
