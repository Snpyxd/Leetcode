class Solution:
    def __init__(self):
        self.ans = []

    def help(self, s, idx):
        self.ans.append("".join(s))

        if idx >= len(s):
            return

        for i in range(idx, len(s)):
            if s[i].isalpha():
                s[i] = s[i].swapcase()

                self.help(s, i + 1)

                s[i] = s[i].swapcase()

    def letterCasePermutation(self, s: str):
        s = list(s)       
        self.help(s, 0)
        return self.ans
