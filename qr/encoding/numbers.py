import re

class Numbers:
    def __init__(self):
        self.re_binary = re.compile('[0-1]+')
        self.re = re.compile('\d+')

    def encode(self, text):
        if not self.re.fullmatch(text):
            raise Exception("Text doesn't match pattern")

        thrpls = [int(text[i:i+3]) for i in range(0, len(text), 3)]

        result = []

        for num in thrpls[:-1]:
            result.append(bin(num)[2:].zfill(10))

        size_last = 10
        if thrpls[-1] < 10:
            size_last = 4
        elif thrpls[-1] < 100:
            size_last = 7

        result.append(bin(thrpls[-1])[2:].zfill(size_last))

        return ''.join(result)
        


    def decode(self, bits):
        if not self.re_binary.fullmatch(bits):
            raise Exception("Text doesn't match pattern")

        parts = [str(int(bits[i:i+10], 2)) for i in range(0, len(bits), 10)]

        return ''.join(parts)
