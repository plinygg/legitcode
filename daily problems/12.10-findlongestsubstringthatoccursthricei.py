# You are given a string s that consists of lowercase English letters.

# A string is called special if it is made up of only a single character. 
# For example, the string "abc" is not special, whereas the strings "ddd", "zz", and "f" are special.

# Return the length of the longest special substring of s which occurs at least thrice, 
# or -1 if no special substring occurs at least thrice.

# A substring is a contiguous non-empty sequence of characters within a string.

class Solution:
    def maximumLength(self, s: str) -> int:
        n = len(s)
        l, r = 1, n

        if not self.helper(s, n, l):
            return -1

        while l + 1 < r:
            mid = (l + r) // 2
            if self.helper(s, n, mid):
                l = mid
            else:
                r = mid

        return l

    def helper(self, s: str, n: int, x: int) -> bool:
        cnt = [0] * 26
        p = 0

        for i in range(n):
            while s[p] != s[i]:
                p += 1
            if i - p + 1 >= x:
                cnt[ord(s[i]) - ord('a')] += 1
            if cnt[ord(s[i]) - ord('a')] > 2:
                return True

        return False