class Solution:
    def encode(self, strs: List[str]) -> str:
        output = []
        for word in strs:
            output.append(f'{len(word)}.{word}')
        return '|'.join(output)

    def decode(self, s: str) -> List[str]:
        num, i, n = [], 0, len(s)
        output = []

        while i < n:
            while s[i] != '.':
                num.append(s[i])
                i += 1
                
            length = int(''.join(num))
            output.append(s[i + 1: i + 1 + length])
            num, i = [], i + 2 + length
            
        return output


