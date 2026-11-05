class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mapping = defaultdict(list)
        
        def freq(word: str) -> Tuple[int]:
            output = [0] * 26
            for c in word:
                output[ord(c) - ord('a')] += 1
            return tuple(output)

        for word in strs:
            mapping[freq(word)].append(word)

        return list(mapping.values())

        