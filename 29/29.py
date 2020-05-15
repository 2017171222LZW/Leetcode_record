给定两个整数，被除数 dividend 和除数 divisor。将两数相除，要求不使用乘法、除法和 mod 运算符。

返回被除数 dividend 除以除数 divisor 得到的商。

示例 1:

输入: dividend = 10, divisor = 3
输出: 3
示例 2:

输入: dividend = 7, divisor = -3
输出: -2

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/divide-two-integers
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

参考我在leetcode写的题解：https://leetcode-cn.com/problems/divide-two-integers/solution/kuai-su-qiu-jie-di-gui-ci-shu-zhi-shu-di-jian-shan/

代码：

class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if (dividend>0 and divisor>0)or(dividend<0 and divisor<0):
            tag = 1
        else:
            tag = -1
        res = self.divCreas(abs(dividend), abs(divisor))
        if tag == -1: res=-res
        if res > 2**31-1:return 2**31-1
        elif res < -2**31:return -2**31
        return res
    def divCreas(self, dividend: int, divisor: int) -> int:
        ex,count = divisor,0
        t,m = 0,1
        if dividend < divisor:
            return 0
        while dividend-t-ex>=0:
            t += ex
            count+=m
            m+=m
            ex+=ex
        if dividend-t>0:
            return count+self.divCreas(dividend-t,divisor)
        return count        
if __name__ == "__main__":
    s = Solution()
    res = s.divide(10,-3)
    print(res)

