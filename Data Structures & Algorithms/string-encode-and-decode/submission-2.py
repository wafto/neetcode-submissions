class Solution:
    def encode(self, strs: List[str]) -> str:
        output = []
        for word in strs:
            output.append(f'{len(word)}.{word}')
        return ''.join(output)

    # 5.Hello5.World


    def decode(self, s: str) -> List[str]:
        i, output, number = 0, [], []

        while i < len(s):
            while s[i] != '.':
                number.append(s[i])
                i += 1
            size = int(''.join(number))
            output.append(s[i + 1: i + 1 + size])
            number = []
            i += size + 1
            
        return output

