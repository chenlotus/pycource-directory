
import os
import prettytable as pt

# 递归获取目录层级及文件个数
def file(level,info,tb):
    if(level):
        if (level[len(level) - 1] != 0):
            level[len(level) - 1] -= 1
            level.append(len(info[1]))
            tb.add_row([len(level) - 1, len(info[2]), info[0]])
        else:
            del level[len(level) - 1]
            file(level,info,tb)


tb = pt.PrettyTable()
tb.field_names = ["层级", "文件数", "路径"]
# 每列对齐方式
tb.align["层级"]  = 'r'
tb.align["文件数"]  = 'r'
tb.align["路径"]  = 'l'
# 层级文件个数初始化
level = [1]
# 为减少处理时间，从当前目录上一级目录开始计算
for info in os.walk('../', topdown=True):
    file(level, info, tb)
print (tb)




