count=0
for i in range(0,20):
    for j in range(0,33):
        for k in range(0,99,3):
            if i+j+k==100 and 5*i+3*j+k//3 == 100:
                count=count+1
                print(str(count)+".公鸡：",i,"母鸡：",j,"小鸡：",k)
                
                


