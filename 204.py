'''
统计所有小于非负整数 n 的质数的数量。

示例 1：

输入：n = 10
输出：4
解释：小于 10 的质数一共有 4 个, 它们是 2, 3, 5, 7 。
示例 2：

输入：n = 0
输出：0
示例 3：

输入：n = 1
'''

# 厄拉多塞
class Solution:
    def countPrimes(self, n: int) -> int:
        if n <= 2:
            return 0
        isPrime = [1] * n
        isPrime[0] = isPrime[1] = 0
        for i in range(2, n):
            if isPrime[i] == 1:
                for j in range(i * i, n, i):
                    isPrime[j] = 0
        return sum(isPrime)
