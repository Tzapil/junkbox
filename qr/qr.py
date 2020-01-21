from encoding.alphabet import Alphabet
from correction import Correction

def main():
    message = 'HELLO'
    print('MESSAGE =', message)

    encoder = Alphabet()

    encoded_message = encoder.encode(message)
    print('ENCODED =', encoded_message)

    decoded_message = encoder.decode(encoded_message)
    print('DECODED =', decoded_message)

    # 0001 DIGITAL
    # 0010 ALPHABET
    # 0100 BYTES
    encoding_algorithm = '0010'

    # DIGITAL  = 10 bits
    # ALPHABET = 9  bits
    # bytes    = 8  bits
    size_len = bin(len(message))[2:].zfill(5)

    fill_8 = ''
    reminder = (len(encoded_message) + 9) % 8
    if reminder != 0:
        fill_8 = fill_8.zfill(8 - reminder)

    # correction L = 152
    block_size = 152
    length = len(encoded_message) + 9 + len(fill_8)
    fill_parts = ('', '11101100', '00010001')
    fill_block = []
    step = 1
    while length < block_size:
        fill_block.append(fill_parts[step])
        length += 8
        step *= -1


    result = ''.join([encoding_algorithm, size_len, encoded_message, fill_8, ''.join(fill_block)])

    print('RESULT = ', len(result), result)

    # QR v1 has only 1 block
    blocks_count = 1
    blocks = [[int(result[i:i+8], 2) for i in range(0, len(result), 8)]]
    print('BLOCKS BYTES = ', blocks)

    # QR v1 and LOW quality = 7
    correction = Correction(7)
    correction_result = correction.encode(blocks)


if __name__ == '__main__':
    main()

class QR:
    def encodeText(self, text):
        pass

    def decode(self):
        pass
