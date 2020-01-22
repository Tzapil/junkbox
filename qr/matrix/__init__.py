search_code_pattern = [
    [1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 1, 1, 0, 1],
    [1, 0, 1, 1, 1, 0, 1],
    [1, 0, 1, 1, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1],
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
            for bit in s_byte:
                step += 1
                setted = False
                while not setted:
                    if self.array[y][x] == 'X':
                        self.array[y][x] = int(step)
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