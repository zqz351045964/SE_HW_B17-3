k = -9
if k >= 0:
    word = str(k) + "正数"
    print(word)
else:
    print(str(k) + "负数")

"""
原程序：
2k = -9
  if 2k>= 0:
    with = 2k +"正数"
        print(with)
    else:
    print(2K+ '负数")

Line 10: 变量名不能以数字开头
Line 11: 变量名不能以数字开头，Python 使用缩进判断语句结构，if 此处缩进应当删除
Line 12: 
with 是一个保留字，不能用于变量名，
with 语句可以用于文件操作、代替 try...except...finally 语句，
k 作为 int 类型不能和 str 类型用加号连接，需要强制转换
Line 13, 14: 缩进
Line 15: 
k 作为 int 类型不能和 str 类型用加号连接，需要强制转换，
单引号和双引号要成对出现，
Python 对变量名大小写敏感，要保持一致
"""