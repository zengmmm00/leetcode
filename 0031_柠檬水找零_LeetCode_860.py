class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        a, b, c = 0, 0, 0  # 5, 10, 20
        for i in bills:
            if i == 5:
                a += 1
            elif i == 10:
                b += 1
                if a == 0:
                    return False
                else:
                    a -= 1
            else:
                c += 1
                if b > 0 and a > 0:
                    b -= 1
                    a -= 1
                elif a >= 3:
                    a -= 3
                else:
                    return False
        return True
