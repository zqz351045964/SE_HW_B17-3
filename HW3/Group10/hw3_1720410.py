#变量名不能以数字开头
# 变量名对大小写敏感，统一变量名
#k作为int型整数不能与字符串进行相加
#int型整数不能与字符串进行相加且引号需前后匹配

k = -9
if k>= 0:
    result = str(k) + "正数"
    print(result)
else:
    print(str(k) + "负数")