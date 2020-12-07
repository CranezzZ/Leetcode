'''
有一个二维矩阵 A 其中每个元素的值为 0 或 1 。

移动是指选择任一行或列，并转换该行或列中的每一个值：将所有 0 都更改为 1，将所有 1 都更改为 0。

在做出任意次数的移动后，将该矩阵的每一行都按照二进制数来解释，矩阵的得分就是这些数字的总和。

返回尽可能高的分数。

 

示例：

输入：[[0,0,1,1],[1,0,1,0],[1,1,0,0]]
输出：39
解释：
转换为 [[1,1,1,1],[1,0,0,1],[1,1,1,1]]
0b1111 + 0b1001 + 0b1111 = 15 + 9 + 15 = 39
'''

class Solution:
    def matrixScore(self, A: List[List[int]]) -> int:
        res = 0
        for row in A:
            if row[0] == 0:
                for j in range(len(row)):
                    row[j] = 1 - row[j]
        for j in range(len(A[0])):
            cnt = 0
            for i in range(len(A)):
                cnt += A[i][j]
            if cnt <= len(A) // 2:
                for i in range(len(A)):
                    A[i][j] = 1 - A[i][j]
        for i in range(len(A)):
            for j in range(len(A[i])):
                res += A[i][j] * 2 ** (len(A[i]) - j - 1)
        return res
