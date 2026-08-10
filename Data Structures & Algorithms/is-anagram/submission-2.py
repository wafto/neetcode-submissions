class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        def frequency(word: str) -> Tuple[int]:
            output = [0] * 32
            for char in word:
                output[ord(char) - ord('a')] += 1
            return tuple(output)

        return frequency(s) == frequency(t)