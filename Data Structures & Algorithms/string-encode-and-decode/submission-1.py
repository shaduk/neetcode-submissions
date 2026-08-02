class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = []
        for word in strs:
            length = len(word)
            encode = str(length) + "#" + word
            encoded.append(encode)
        return ''.join(encoded)

    def decode(self, s: str) -> List[str]:
        start = 0
        decoded = []
        length = ''
        while start < len(s):
            if s[start] == "#":
                length_int = int(length)
                decoded.append(s[start+1:start+length_int+1])
                start += length_int + 1
                length = ''
            else:
                length += s[start]
                start = start + 1
        return decoded