import re

class Alphabet:
    def __init__(self):
        self.re_binary = re.compile('[0-1]+')
        self.re = re.compile('[A-Z0-9\s$%*+-./:]+')

        self.table = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ $%*+-./:'

    def get_code(self, symbol):
        return self.table.index(symbol)

    def generate_pair_code(self, pair):
        code = self.get_code(pair[0]) * 45 + self.get_code(pair[1])

        return bin(code)[2:].zfill(11)

    def encode(self, text):
        text = text.upper()
        if not self.re.fullmatch(text):
            raise Exception("Text doesn't match pattern")

        parts = [text[i:i+2] for i in range(0, len(text), 2)]        

        result = []

        for pair in parts[:-1]:
            result.append(self.generate_pair_code(pair))

        if len(parts[-1]) == 1:
            result.append(bin(self.get_code(parts[-1]))[2:].zfill(6))
        else:
            result.append(self.generate_pair_code(parts[-1]))

        return ''.join(result)
        


    def decode(self, bits):
        if not self.re_binary.fullmatch(bits):
            raise Exception("Text doesn't match pattern")

        parts = [int(bits[i:i+11], 2) for i in range(0, len(bits), 11)]

        result = []

        for part in parts:
            first = int(part / 45)
            second = part % 45

            if part > 45:
                result.append(self.table[first])
            result.append(self.table[second])

        return ''.join(result)