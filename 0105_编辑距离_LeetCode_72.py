class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        if len(word1) < len(word2):
            tmp = word1
            word1 = word2
            word2 = tmp
        dis = [i for i in range(len(word1) + 1)]
        for i in range(len(word2)):
            w2 = word2[i]
            new_dis = [i + 1]
            for j in range(len(word1)):
                w1 = word1[j]
                if w2 == w1:
                    new_dis.append(dis[j])
                else:
                    new_dis.append(min(new_dis[-1], min(dis[j], dis[j + 1])) + 1)
            dis = new_dis
        return dis[-1]
