class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        freq1, freq2 = [0] * 26, [0] * 26
        
        for i in range(len(s)):
            freq1[ord(s[i]) - ord('a')] += 1
            freq2[ord(t[i]) - ord('a')] += 1

        return freq1 == freq2
        