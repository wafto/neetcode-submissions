class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        def freq(word: str) -> Tuple[int]:
            output = [0] * 26
            for c in word:
                output[ord(c) - ord('a')] += 1
            return tuple(output)

        return len(s) == len(t) and freq(s) == freq(t)
        