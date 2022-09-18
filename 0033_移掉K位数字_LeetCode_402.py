class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        if len(num) == k:
            return '0'
        record = []
        for i in range(10):
            record.append([])
        for i in range(k):
            record[int(num[i])].append(i)

        res = ''
        p = k
        for i in range(len(num) - k):
            record[int(num[p])].append(p)
            m = None
            for j in range(10):
                if len(record[j]) != 0:
                    m = j
                    b = record[j].pop(0)
                    for a in range(10):
                        while len(record[a]) != 0 and record[a][0] < b:
                            record[a].pop(0)
                    break
            res += str(m)
            p += 1
        return str(int(res))
