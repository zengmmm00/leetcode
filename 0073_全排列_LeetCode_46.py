class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        visit = {n: False for n in nums}
        self.dfs(nums, [], res, visit)
        return res

    def dfs(self, nums, sub, res, visit):
        if len(sub) == len(nums):
            res.append(sub.copy())
        else:
            for i in range(len(nums)):
                if not visit[nums[i]]:
                    sub.append(nums[i])
                    visit[nums[i]] = True
                    self.dfs(nums, sub, res, visit)
                    sub.pop()
                    visit[nums[i]] = False
