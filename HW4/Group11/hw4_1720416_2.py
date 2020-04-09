//共90只脚，都是鸡45只，都是兔23只
for x in range(0, 45):
    for y in range(0, 23):
        if (x + y == 30) and (x*2 + y*4 == 90):
            print('鸡：%s 只，兔：%s 只' % (x, y))
