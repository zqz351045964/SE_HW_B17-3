# 变量名不能以数字开头
k2 = -9
if k2 >= 0:
    # with是标识符不能作为变量名
    # k2是int型格式，不能直接与字符串类型相加，要先将k2转换为字符串类型才能相加
    with1 = str(k2) + "正数"
    print(with1)
else:
    # if else语句是以缩进来判断函数内容，不饿能随便缩进或不缩进
    # 字符串的定义可以用双引号也可以用单引号，但是不能混着用
    print(str(k2) + "负数")
