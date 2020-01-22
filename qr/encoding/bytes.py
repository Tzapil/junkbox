class Bytes:
    def encode(self, text):
        return bytes(text, 'utf-8')
    def decode(self, bytes):
        return str(bytes, 'utf-8')