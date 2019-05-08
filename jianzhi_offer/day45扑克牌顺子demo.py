# Author: Baozi
#-*- codeing:utf-8 -*-
"""题目描述
LL今天心情特别好,因为他去买了一副扑克牌,发现里面居然有2个大王,2个小王(一副牌原本是54张^_^)...
他随机从中抽出了5张牌,想测测自己的手气,看看能不能抽到顺子,如果抽到的话,他决定去买体育彩票,嘿嘿！
“红心A,黑桃3,小王,大王,方片5”,“Oh My God!”不是顺子.....LL不高兴了,他想了想,决定大\小王可以
看成任何数字,并且A看作1,J为11,Q为12,K为13。上面的5张牌就可以变成“1,2,3,4,5”(大小王分别看作2和4),
“So Lucky!”。LL决定去买体育彩票啦。 现在,要求你使用这幅牌模拟上面的过程,然后告诉我们LL的运气如何，
如果牌能组成顺子就输出true，否则就输出false。为了方便起见,你可以认为大小王是0
"""
"""解题思路：
    我们可以把5张牌看成由5个数字组成的数组。大小王是特殊的数字，我们不妨把它定义成0，这样
就能和其他的扑克牌区分出来。
    接下来我们分析怎么判断5个数字是不是连续的，最直观的方法就是把数组排序。值得注意的是，
由于0可以当成任意数字，即相邻的两个数字相隔若干个数字，但我们若有足够的0可以补满这两个数字
的空缺，这个数组实际上还是连续的。
    于是我们需要做3件事情：首先把数组排序，再统计数组中0的个数，最后统计排序之后的数组中相邻
数字之间的空缺总数。如果空缺的总数小于或者等于0的个数，那么这个数组就是连续的，反之不是连续的。
"""
class Solution:
    def IsContinuous(self, numbers):
        if not numbers or not isinstance(numbers,list) or len(numbers) != 5:
            return False
        print(numbers)
        numbers.sort()
        print(numbers)
        NumberOf0 = 0
        for i in numbers:
            if i == 0:
                NumberOf0 += 1
        print(NumberOf0)

        NumberOfGap = 0
        start,last = NumberOf0,NumberOf0+1#注意统计间隔的时候要从非0数字开始统计！
        while last<len(numbers):
            if numbers[last] == numbers[start]:
                return False
            NumberOfGap += numbers[last] - numbers[start] - 1
            last += 1
            start += 1
        # print("NumberOf0",NumberOf0)
        # print("NumberOfGap",NumberOfGap)
        if NumberOfGap>NumberOf0:
            return False
        return True

if __name__ == '__main__':
    # nums = [0,1,3,3,5]
    # nums = [1,3,2,6,4]
    nums = [0,3,2,6,4]
    s = Solution()
    print(s.IsContinuous(nums))
