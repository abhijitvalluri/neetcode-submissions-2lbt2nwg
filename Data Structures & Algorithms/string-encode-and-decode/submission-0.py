class Solution:

    def encode(self, strs: List[str]) -> str:
        output = ""

        for string in strs:
            length = len(string)
            output += str(length) + "." + string
        
        return output

    def decode(self, s: str) -> List[str]:
        length = 0
        word_building = False
        output = []
        word = ""
        for c in s:
            if not word_building and c.isdigit():
                length = length * 10 + ord(c) - ord('0')
            elif not word_building and c == ".":
                word_building = True
            elif length > 0:
                word += c
                length -= 1
                if length == 0:
                    output.append(word)
                    word = ""
                    word_building = False
        
        return output
