def cal():
    for chick in range(46):
        for rabbit in range(23):
            if(chick + rabbit == 30 and chick*2 + rabbit*4 ==90):
                print("鸡有{}只, 兔有{}只".format(chick, rabbit))

cal()
