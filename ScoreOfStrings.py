class Solution:
    def scoreOfString(self, s: str) -> int:
        length = len(s)
        total = 0
        for i in range (length-1):
            total += abs(ord(s[i]) - ord(s[i+1]))
        return total
