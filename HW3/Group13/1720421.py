#变量名必须以字母或下划线开头
k=-9
if k>=0:
#不能是int+string的组合
    t=str(k)+"正数"
    print(t)
else:
#print里面引号前后一致
    print(str(k)+"负数")
