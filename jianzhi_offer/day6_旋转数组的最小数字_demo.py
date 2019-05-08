# Author: Baozi
#-*- codeing:utf-8 -*-
"""题目描述
把一个数组最开始的若干个元素搬到数组的末尾，我们称之为数组的旋转。
输入一个非减排序的数组的一个旋转，输出旋转数组的最小元素。
例如数组{3,4,5,1,2}为{1,2,3,4,5}的一个旋转，该数组的最小值为1。
NOTE：给出的所有元素都大于0，若数组大小为0，请返回0。
"""
class Soultion:
    def __init__(self):
        pass

    def Searchmin(self,arr):
        if not arr or len(arr) == 0:
            return None
        start = 0
        l = len(arr)
        end = l - 1
        if (arr[start] < arr[end]):
            return arr[start]
        mid = int((start + end) / 2)
        result = arr[start]
        #该情况下顺序遍历
        if(arr[mid] == arr[start] and arr[start] == arr[end]):
            for i in range(1,l):
                if(arr[i]<result):
                    result = arr[i]
            return result
        print("#"*30)

        while(arr[start] >= arr[end]):
            mid = int((start + end) / 2)
            if(end - start == 1):
                result = arr[end]
                break
            if(arr[mid]>arr[end]):
                start = mid
            elif(arr[mid]<arr[end]):
                end = mid
        return result

if __name__ == '__main__':
    arr0 = [4,5,1,2,3]
    arr1 = [1,0,1,1,1]
    arr2 = [1,1,1,0,1]
    arr3 = []
    arr4 = [1,2,3,4,5]
    t=Soultion()
    print(t.Searchmin(arr0))
    print(t.Searchmin(arr1))
    print(t.Searchmin(arr2))
    print(t.Searchmin(arr3))
    print(t.Searchmin(arr4))
