class Solution:
    def maxProduct(self, words: List[str]) -> int:
        res = 0
        have = []
        for i in range(len(words)):
            have.append([False] * 26)
        for i in range(len(words)):
            for w in words[i]:
                have[i][ord(w) - ord('a')] = True
        for i in range(len(words)):
            for j in range(i + 1, len(words)):
                tmp = len(words[i]) * len(words[j])
                if tmp > res:
                    f = True
                    for w in words[j]:
                        if have[i][ord(w) - ord('a')] == True:
                            f = False
                            break
                    if f:
                        res = tmp
        return res


'''
先计算长度的乘积，再判断两个words是否符合条件
'''
