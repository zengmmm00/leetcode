class Solution:
    def combinationSum2(self, candidates, target: int):
        candidates = sorted(candidates)
        res = []
        self.backtracking(candidates, [], 0, 0, target, res)
        return res

    def backtracking(self, candidates, sub, k, s, target, res):
        if s == target:
            res.append(sub.copy())
            return

        if len(sub) == len(candidates):
            return

        i = k

        while i < len(candidates):
            put = candidates[i]
            new_sub = sub + [put]
            new_s = s + put
            if new_s > target:
                break

            self.backtracking(candidates, new_sub.copy(), i + 1, new_s, target, res)
            i += 1
            while i < len(candidates) and candidates[i - 1] == candidates[i]:
                i += 1


'''
避免重复的组合：要避免同一深度下，选择相同的值。
递归调用函数的时候，argument要传list.copy()；如果传的是list，在调用完函数后要把加入list的元素拿出来。
'''
