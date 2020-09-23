import random

target = random.randint(1, 100)

count = 0
while True:
    n = int(input('请猜一个1-100的数字：'))
    if target < n:
        print('猜大了')
        count += 1
    elif target > n:
        print('猜小了')
        count += 1
    else:
        print('猜对了，恭喜您')
        break
    if count == 6:
        print('已经猜测5次，您输了')
        break