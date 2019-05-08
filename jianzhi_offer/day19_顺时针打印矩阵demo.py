# Author: Baozi
#-*- codeing:utf-8 -*-
"""题目描述
输入一个矩阵，按照从外向里以顺时针的顺序依次打印出每一个数字，
例如，如果输入如下4 X 4矩阵： 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16
则依次打印出数字1,2,3,4,8,12,16,15,14,13,9,5,6,7,11,10.
"""
class Solution:
    # matrix类型为二维列表，需要返回列表
    def printMatrix(self, matrix):
        # write code here
        if not isinstance(matrix, list):
            return None
        row, col = len(matrix), len(matrix[0])
        start = 0
        ret = []
        while row > start*2 and col > start*2:
            self.PrintCircleNumber(matrix,row,col,start,ret)
            start += 1
        return ret

    def PrintCircleNumber(self,matrix,row,col,start,ret):
        rNum = row-start
        cNum = col-start
        # sNum = 2*start
        #打印第一行,即圈圈的最上面一横
        for i in range(start,cNum):
            print(matrix[start][i],end=' ')
            ret.append(matrix[start][i])
        #打印最后一列，即圈圈的右边一竖
        if rNum-1 > start:
            for i in range(start+1,rNum):#注意range的区间范围是左开右闭
                print(matrix[i][cNum-1],end=' ')
                ret.append(matrix[i][cNum-1])
        #打印最后一行，即圈圈的下面一横
        if rNum-1 > start and cNum-2 > start:
            for i in range(cNum-2,start-1,-1):
                print(matrix[rNum-1][i],end=' ')
                ret.append(matrix[rNum-1][i])
        #打印第一列，即圈圈的左边一竖
        if cNum-1 > start and rNum-2 > start:
            for i in range(rNum-2,start,-1):
                print(matrix[i][start],end=' ')
                ret.append(matrix[i][start])


if __name__ == '__main__':
    # matrix = [[1]]
    # matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
    # matrix = [[1],[2],[3],[4]]
    matrix = [[1,2,3,4]]
    s = Solution()
    r = s.printMatrix(matrix)
    print(r)