class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left, longest = 0, 0
        mapping = dict()

        for right in range(len(s)):
            mapping[s[right]] = 1 + mapping.get(s[right], 0)

            while right - left + 1 - max(mapping.values()) > k:
                mapping[s[left]] -= 1
                left += 1

            longest = max(longest, right - left + 1)

        return longest