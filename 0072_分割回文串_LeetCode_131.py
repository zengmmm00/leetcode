class Solution:
    def partition(self, s: str) -> List[List[str]]:
        global palindrome
        palindrome = dict()
        res = []
        self.dfs(s, [s], 1, res)
        return res

    def dfs(self, s, sub, cut, res):
        global palindrome

        if cut == len(s):
            for i in range(len(sub)):
                if sub[i] in palindrome:
                    p = palindrome[sub[i]]
                else:
                    p = self.isPalindrome(sub[i])
                    palindrome[sub[i]] = p
                if not p:
                    return
            res.append(sub.copy())
            return
        else:
            word = sub[-1]

            # cut
            sub.pop()
            left = word[:cut - len(s)]
            sub.append(left)
            right = word[cut - len(s):]
            sub.append(right)
            self.dfs(s, sub, cut + 1, res)
            sub.pop()
            sub.pop()
            sub.append(word)

            # no cut
            self.dfs(s, sub, cut + 1, res)

    def isPalindrome(self, s):
        if len(s) == 1:
            return True
        else:
            m = int(len(s) / 2)
            if len(s) % 2 == 1:
                s = s[:m] + s[m + 1:]

            m = int(len(s) / 2)

            lw = s[:m]
            rw = s[m:]
            rw = rw[::-1]
            if lw == rw:
                return True
            else:
                return False
