class Solution:

    def encode(self, strs: List[str]) -> str:
        output = []
        for word in strs:
            output.append(f'{len(word)}#{word}')
        return ''.join(output)

    def decode(self, s: str) -> List[str]:
        size, output, index = '', [], 0

        while index < len(s):
            if s[index] != '#':
                size += s[index]
                index += 1
            else:
                length, size = int(size), ''
                output.append(s[index + 1: index + length + 1])
                index += length + 1

        return output


