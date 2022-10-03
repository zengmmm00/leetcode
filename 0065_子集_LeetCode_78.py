class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        global res
        res = []
        sub = []
        self.backtracking(0, nums, sub)
        return res

    def backtracking(self, i, nums, sub):
        global res
        if i <= len(nums):
            res.append(sub.copy())
            for j in range(len(nums)):
                if nums[j] not in sub:
                    sub.append(nums[j])
                    self.backtracking(i + 1, nums, sub)
                    sub.pop()
                else:
                    break


'''
向subset加入新元素之前要判断新元素是否已经存在，如果已经存在，要break循环。
'''
