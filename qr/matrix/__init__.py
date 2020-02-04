search_code_pattern = [
    [1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 1, 1, 0, 1],
    [1, 0, 1, 1, 1, 0, 1],
    [1, 0, 1, 1, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1],
]

masks = [
    lambda x, y: (x + y) % 2,
    lambda x, y: y % 2,
    lambda x, y: x % 3,
    lambda x, y: (x + y) % 3,
    lambda x, y: (x // 3 + y // 2) % 2,
    lambda x, y: (((x * y) % 2) + ((x * y) % 3)) % 2,
    lambda x, y: (((x * y) % 3) + ((x * y) % 2)) % 2,
]

class Matrix:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.array = [['X' for _ in range(y)] for _ in range(x)]

    def __str__(self):
        return '\n'.join([' '.join([str(x).ljust(4) for x in row]) for row in self.array])
    
    def get_array(self):
        return self.array

    def add_sync_lines(self):
        for i in range(self.x):
            if self.array[6][i] == 'X':
                self.array[6][i] = 1 if i % 2 == 0 else 0
            if self.array[i][6] == 'X':
                self.array[i][6] = 1 if i % 2 == 0 else 0

    def add_search_codes(self):
        self.add_search_code(0, 0)
        self.add_search_code(0, self.y - 7)
        self.add_search_code(self.x - 7, 0)

    def get_text(self):
        square = b'\xe2\x96\xa0'.decode()
        white = b'\xe2\x97\xbb'.decode()
        result = '\n'.join([' '.join([str(x) for x in row]) for row in self.array])
        result = result.replace('X', white).replace('0', white).replace('1', square)
        return result

    def get_svg(self):
        size = 500
        length = 21
        point_size = size // (length + 4)
        point_t = '<rect fill="{color}" x="{x}px" y="{y}px" width="{w}px" height="{h}px"/>'
        array = []
        for y, row in enumerate(self.array):
            r = []
            for x, point in enumerate(row):
                # 0 "white"
                # 1 "black"
                color = "white"
                if point == 1:
                    color = "black"
                r.append(point_t.format(color=color, w=point_size, h=point_size, x=(x + 2) * point_size, y=(y + 2) * point_size))
            array.append(''.join(r))
        field = ''.join(array)
        return f'<svg version="1.1" id="Layer_1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" x="0px" y="0px"  height="{size}px" width="{size}px">{field}</svg>'
    
    def mask_and_correction(self):
        # LOW + 0 MASK
        code = '111011111000100'

        # ALWAYS BLACK
        self.array[self.y - 8][8] = 1

        self.mask_upper(code)
        self.mask_lower(code)

    def mask_upper(self, code):
        y = 8
        x = 8
        step = 0
        for i in range(8):
            if self.array[y][i] == 'X':
                self.array[y][i] = int(code[step])
                step += 1

        for i in range(8, -1, -1):
            if self.array[i][x] == 'X':
                self.array[i][x] = int(code[step])
                step += 1

    def mask_lower(self, code):
        y = 8
        x = 8
        step = 0
        for i in range(7):
            if self.array[self.y - 1 - i][x] == 'X':
                self.array[self.y - 1 - i][x] = int(code[step])
                step += 1

        for i in range(7, -1, -1):
            if self.array[y][self.x - 1 - i] == 'X':
                self.array[y][self.x - 1 - i] = int(code[step])
                step += 1

    def mask(self, x, y, value, version=0):
        current_mask = masks[version]
        if current_mask(x, y) == 0:
            if value == 1:
                return 0
            return 1
        return value

    def add_search_code(self, x, y):
        n = 7
        for i in range(7):
            for j in range(n):
                self.array[x + i][y + j] = search_code_pattern[i][j]

        for i in range(8):
            c_x = x + i
            c_y = y + i
            if c_y < self.y:
                if x - 1 >= 0:
                    self.array[x - 1][y + i] = 0
                if x + 7 < self.x:
                    self.array[x + 7][y + i] = 0
            if c_x < self.x:
                if y - 1 >= 0:
                    self.array[x + i][y - 1] = 0
                if y + 7 < self.y:
                    self.array[x + i][y + 7] = 0

    def fill_with_data(self, data):
        v_direction = 'up'
        h_direction = 'left'
        x, y = self.x - 1, self.y - 1

        step = 0

        for byte in data:
            s_byte = bin(byte)[2:].zfill(8)
            print('NEXT_BYTE=', s_byte)
            for bit in s_byte:
                step += 1
                setted = False
                while not setted:
                    isX = self.array[y][x] == 'X'
                    if step == 7:
                        print(x, y, int(bit), self.mask(x, y, int(bit), 0))
                    if isX:
                        # int(step)
                        self.array[y][x] = self.mask(x, y, int(bit), 0)
                        setted = True
                    if v_direction == 'up':
                        if h_direction == 'left':
                            h_direction = 'right'
                            x -= 1
                        elif h_direction == 'right':
                            h_direction = 'left'
                            x += 1
                            y -= 1

                        if y < 0:
                            v_direction = 'down'
                            h_direction = 'left'
                            x -= 2
                            y = 0
                    elif v_direction == 'down':
                        if h_direction == 'left':
                            h_direction = 'right'
                            x -= 1
                            if x == 5:
                                x -= 1
                        elif h_direction == 'right':
                            h_direction = 'left'
                            x += 1
                            y += 1

                        if y >= self.y:
                            v_direction = 'up'
                            h_direction = 'left'
                            y = self.y - 1
                            x -= 2

# def add_search_codes(matrix):
#     return [
#         0b1111111,
#         0b1000001,
#         0b1011101,
#         0b1011101,
#         0b1011101,
#         0b1000001,
#         0b1111111,
#     ]