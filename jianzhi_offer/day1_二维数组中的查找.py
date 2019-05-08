# Author: Baozi
#-*- codeing:utf-8 -*-
"""题目描述
在一个二维数组中（每个一维数组的长度相同），每一行都按照从左到右递增的顺序排序，每一列都按照从上到下递增的顺序排序。
请完成一个函数，输入这样的一个二维数组和一个整数，判断数组中是否含有该整数
"""
import random
array = [[1,2,8,9],[2,4,9,12],[4,7,10,13],[6,8,11,15]]
target = random.randint(1,20)
# target = 14
print("array :",array)
print("target :",target)
# 二维行列式的行
row_index = len(array)
# 二维行列式的列
col_index = len(array[0])
if target > array[row_index - 1][col_index - 1]:
    print("Out of the array range!")
    exit(0)

def search_array(array,target):
    result = False
    row = 0;col = col_index-1
    tmp = array[row][col]
    while(row < row_index-1 and col >= 0):
        if(tmp == target):
            result = True
            break
        elif tmp > target:
            col -= 1
            tmp = array[row][col]
        else:
            row += 1
            tmp = array[row][col]
    return result

if __name__ == '__main__':
    result = search_array(array,target)
    print("result :",result)

