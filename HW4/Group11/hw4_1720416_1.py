//公鸡最多可买20只，母鸡最多可买33只。公鸡x，母鸡y，小鸡z。
count = 0
for x in range(0, 20):
    for y in range(0, 33):
        z = 100-x-y
        if (z%3 == 0) & (5*x + 3*y + z/3 == 100):
            print('公鸡：%s 只，母鸡：%s 只，小鸡：%s 只' %(x,y,z))
            count = count+1
print('---')
print('共有 %d 种买法' % count)
