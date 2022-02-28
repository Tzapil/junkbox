from encoding.alphabet import Alphabet
from correction import Correction
from matrix import Matrix

def main():
    message = 'HELLO'
    print('MESSAGE =', message, len(message))

    encoder = Alphabet()

    encoded_message = encoder.encode(message)
    print('ENCODED =', encoded_message, len(encoded_message))
    print('ETALON  =', '0110000101101111000110011000')

    decoded_message = encoder.decode(encoded_message)
    print('DECODED =', decoded_message, len(decoded_message))

    # 0001 DIGITAL
    # 0010 ALPHABET
    # 0100 BYTES
    encoding_algorithm = '0010'

    # DIGITAL  = 10 bits
    # ALPHABET = 9  bits
    # bytes    = 8  bits
    # size_len = bin(len(encoded_message))[2:].zfill(9)
    size_len = bin(len(message))[2:].zfill(9)
    print('SIZE_LEN=', size_len, len(size_len), len(encoded_message) + 9 + 4)
    # 000011100 41
    # 000000101 5 (5 символов в сообщении?)

    encoded_message = ''.join([encoding_algorithm, size_len, encoded_message])

    print('FULL_MESSAGE=', encoded_message, len(encoded_message))

    fill_8 = ''
    reminder = len(encoded_message) % 8
    if reminder != 0:
        fill_8 = fill_8.zfill(8 - reminder)

    # correction L = 152
    block_size = 152
    length = len(encoded_message) + len(fill_8)
    fill_parts = ('', '11101100', '00010001')
    fill_block = []
    step = 1
    while length < block_size:
        fill_block.append(fill_parts[step])
        length += 8
        step *= -1

    result = ''.join([encoded_message, fill_8, ''.join(fill_block)])

    print('RESULT = ', result, len(result))

    # QR v1 has only 1 block
    blocks_count = 1
    blocks = [[int(result[i:i+8], 2) for i in range(0, len(result), 8)]]
    print('BLOCKS BYTES = ', blocks, len(blocks[0]))

    # QR v1 and LOW quality = 7
    correction = Correction(7)
    correction_result = correction.encode(blocks)

    print('CORRECTION RESULT=', correction_result, len(correction_result))
    # QR v2 and HIGH quality = 28
    correction2 = Correction(28)
    correction_check = correction2.encode([[64, 196, 132, 84, 196, 196, 242, 194, 4, 132, 20, 37, 34, 16, 236, 17]])
    print('CORRECTION CHECK=', correction_check, len(correction_check))

    # QR v1 = 21x21
    matrix = Matrix(21, 21)
    matrix.add_search_codes()
    matrix.add_sync_lines()
    matrix.mask_and_correction()
    matrix.fill_with_data(correction_result)
    print(matrix)
    print(matrix.get_text())

    svg = matrix.get_svg()
    with open('qr.svg', 'w') as file:
        file.write(svg)



if __name__ == '__main__':
    main()

class QR:
    def encodeText(self, text):
        pass

    def decode(self):
        pass
