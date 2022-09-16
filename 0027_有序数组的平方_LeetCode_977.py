class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        neg = []
        pos = []
        for x in nums:
            if x < 0:
                neg.insert(0, x ** 2)
            else:
                pos.append(x ** 2)
        res = []
        for i in range(len(nums)):
            if len(neg) == 0:
                res += pos
                break
            elif len(pos) == 0:
                res += neg
                break
            else:
                if neg[0] < pos[0]:
                    res.append(neg[0])
                    neg.pop(0)
                else:
                    res.append(pos[0])
                    pos.pop(0)
        return res
