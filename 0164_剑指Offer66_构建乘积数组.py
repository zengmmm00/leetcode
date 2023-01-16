class Solution:
    def constructArr(self, a: List[int]) -> List[int]:
        front = [1]
        for num in a:
            front.append(front[-1] * num)
        back = [1]
        for num in a[::-1]:
            back.append(back[-1] * num)
        result = []
        for i in range(len(a)):
            result.append(front[i] * back[len(a) - 1 - i])
        return result
