题目：请指出一下程序的错误之处,并修改正确。
    
 2k = -9
  if 2k>= 0:
    with = 2k +"正数"
        print(with)
    else:
    print(2K+ '负数")

#首先数字不能作为开头；
#if后没有缩进；
#'负数”应该使用双引号而不是一半单引号，一半双引号，且书写时单双引号该各自配对；
#变量名不能使用特殊字符，with属于特殊字符；
#k作为int型整数不能与字符串进行相加，且前后大小书写不统一。
#修改后：
    k = -9
    if k >=0:
       lxy = str(k) + "正数"
           print(lxy)
    else:
    print(skr(k) + "负数")


        
