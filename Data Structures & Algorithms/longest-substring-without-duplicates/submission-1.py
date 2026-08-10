class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left, longest = 0, 0
        seen = set()

        for right, char in enumerate(s):
            while char in seen:
                seen.remove(s[left])
                left += 1 

            seen.add(char)
            longest = max(longest, len(seen))

        return longest
        

            