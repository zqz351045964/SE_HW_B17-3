"""
错误：
1、变量命名以数字开头（2k）
2、使用了Python关键字作为变量名（with）
3、if和else未配对（缩进不同）
4、变量名没有对应（上面用的是'2k'，下面print中用的是'2K'）
5、字符串单引号与双引号混用（'负数"）
6、直接将int类型与字符串类型相加，无法自动转换为字符串，需要使用str()函数将int类型转化为str类型（2k +"正数"）
"""

"""修改前
2k = -9

  if 2k>= 0:

    with = 2k +"正数"

        print(with)

    else:

    print(2K+ '负数")
"""

#修改后
k = -9
if k>=0:
    wit = str(k) + "正数"
    print(wit)
else:
    print(str(k) + "负数")
