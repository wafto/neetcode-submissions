class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left, longest, frequent = 0, 0, 0
        mapping = defaultdict(int)

        for right, char in enumerate(s):
            mapping[char] += 1
            frequent = max(frequent, mapping[char])

            while (right - left + 1) > frequent + k:
                mapping[s[left]] -= 1
                left += 1

            longest = max(longest, right - left + 1)

        return longest

