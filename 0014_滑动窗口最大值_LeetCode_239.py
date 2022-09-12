class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        window = []
        for i in range(k):
            if len(window) == 0:
                window.append(dict({'index': i, 'value': nums[i]}))
            else:
                while len(window) != 0 and window[-1]['value'] < nums[i]:
                    del window[-1]
                window.append(dict({'index': i, 'value': nums[i]}))
        if len(window) == 0:
            return []
        res = [window[0]['value']]
        for i in range(k, len(nums)):
            if window[0]['index'] == i - k:
                del window[0]
            while len(window) != 0 and window[-1]['value'] < nums[i]:
                del window[-1]
            window.append(dict({'index': i, 'value': nums[i]}))
            res.append(window[0]['value'])
        return res


'''
窗口用双端递减队列。
字典带一个元素新建:dict({'index': i, 'value': nums[i]})，不要漏掉{}
获取字典某个元素的value：<dict>['<value name>']
'''