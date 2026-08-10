class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        def frequency(word: str) -> Tuple[int]:
            output = [0] * 32
            for char in word:
                output[ord(char) - ord('a')] += 1
            return tuple(output)
        
        groups = defaultdict(list)

        for word in strs:
            groups[frequency(word)].append(word)

        return [group for group in groups.values()]
