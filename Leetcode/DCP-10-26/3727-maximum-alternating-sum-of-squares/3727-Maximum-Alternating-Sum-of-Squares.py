
class Solution:
    def maxAlternatingSum(self, nums: list[int]) -> int:
        squares = sorted([x * x for x in nums], reverse=True)

        n = len(nums)
        positive = (n + 1) // 2

        ans = sum(squares[:positive]) - sum(squares[positive:])

        return ans