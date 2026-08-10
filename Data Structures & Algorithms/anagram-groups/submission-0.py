class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        output = dict()

        for word in strs:
            key = list(word)
            key.sort()
            key = ''.join(key)
            if key not in output:
                output[key] = []
            output[key].append(word)

        return list(output.values())
            
