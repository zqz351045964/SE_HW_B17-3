def buy():
    for cock in range(21):
        for hen in range(33):
            for chick in range(3,100):
                if (cock*5 + hen*3 + chick/3 == 100 and cock + hen + chick == 100 and chick%3 == 0):
                    print("公鸡:{}只 母鸡:{}只 小鸡{}只".format(cock, hen, chick))
    
buy()
                
