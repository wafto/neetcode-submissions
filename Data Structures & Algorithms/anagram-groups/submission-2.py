class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)

        def frequency(word: str) -> Tuple[int]:
            output = [0] * 26
            for char in word:
                output[ord(char) - ord('a')] += 1
            return tuple(output)

        for word in strs:
            groups[frequency(word)].append(word)

        return [group for group in groups.values()]