# Author: Baozi
#-*- codeing:utf-8 -*-
"""题目描述
请实现一个函数用来判断字符串是否表示数值（包括整数和小数）。
例如，字符串"+100","5e2","-123","3.1416"和"-1E-16"都表示数值。
但是"12e","1a3.14","1.2.3","+-5"和"12e+4.3"都不是。
"""
"""解题思路：
根据题目给出的规则，可以表示成数值的字符串类型有：int类型，float浮点型，指数型(e和E)，当然，前面三种都可以带上
正负号。我们可以通过遍历一遍字符串判断该字符串是否含有e/E，如果有e则只能有一个且不能是最后一个，小数点不能重复
出现或出现在e之后，重复出现符号时，第二个符号下标位置必须大于0且必须跟在e后面。
"""
class Solution:
    # s字符串
    def isNumeric(self, s):
        # write code here
        if not s or len(s) == 0:
            return False
        #用于判断是否含有E
        hasE = False
        #用于判断是否含有小数点
        hasDecimal = False
        #用于判断是否含有符号
        hasSign = False

        for i in range(len(s)):
            if s[i] == '.':
                # 小数点不能重复出现或和e共线
                if hasE or hasDecimal:
                    return False
                hasDecimal = True
            elif s[i] == 'e' or s[i] == 'E':
                # 如果有e则只能有一个且不能是最后一个
                if hasE or i == len(s)-1:
                    return False
                hasE = True
            elif s[i] == '+'or s[i] == '-':
                #重复出现符号时应该在e/E后面，或者在最开始的位置
                if hasSign and s[i-1] != 'e' and s[i-1] != 'E':
                    return False
                #下面这种情况用于判断数值在最开始不包含正正负号的情况
                if not hasSign and i>0 and s[i-1] != 'e' and s[i-1] != 'E':
                    return False
                hasSign = True
            elif s[i] < '0' or s[i] > '9':
                return False
        return True


if __name__ == '__main__':
    s = Solution()
    test = '123.45e+6'
    print(s.isNumeric(test))
