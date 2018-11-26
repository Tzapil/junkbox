import re
import requests

class Number:
    def __init__(self, str):
        nums = re.compile(r'^[0-9oxa-f]+$')
        english = re.compile(r'^[a-z\s]+$')
        roman = re.compile(r'^[IVXLCDM]+$')
        self.num = None
        if type(str) is int:
            self.num = str
        elif nums.match(str):
            self.num = self.parse_num(str)
        elif english.match(str):
            self.num = self.parse_english(str)
        elif roman.match(str):
            self.num = self.parse_roman(str)
        else:
            self.num = self.parse_russian(str)

    def __add__(self, other):
        return Number(self.get_num() + other.get_num())

    def __mul__(self, other):
        return Number(self.get_num() * other.get_num())

    def __sub__(self, other):
        return Number(self.get_num() - other.get_num())

    def __truediv__(self, other):
        print(self.get_num() / other.get_num())
        return Number(int(self.get_num() / other.get_num()))

    def __str__(self):
        return str(self.get_num())

    def get_num(self):
        return self.num

    def parse_num(self, num):
        return int(num, 0)

    def parse_roman(self, num):
        nums = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        sum = 0
        biggest = 0
        for ch in num[::-1]:
            curr = nums[ch]
            if curr < biggest:
                sum -= curr
            else:
                sum += curr
            biggest = curr if curr > biggest else biggest
        
        return sum
    
    def parse_english(self, num):
        tens = ['twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']
        units = ['zero', 'one', 'two', 'three', 'four','five','six','seven','eight',"nine", 'ten','eleven','twelve',
                 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']
        scales = ['hundred', 'thousand', 'million', 'billion']

        numwords = {'and': (1, 0)}

        # make tuples
        for idx, word in enumerate(units): numwords[word] = (1, idx)
        for idx, word in enumerate(tens): numwords[word] = (1, (idx + 2) * 10)
        for idx, word in enumerate(scales): numwords[word] = (10 ** (idx * 3 or 2), 0)

        current = result = 0
        for word in num.split():
            scale, increment = numwords[word]
            current = current * scale + increment
            if scale > 100:
                result += current
                current = 0

        return result + current

    def parse_russian(self, num):
        units = {
            u'ноль': 0,
            u'один': 1,
            u'одна': 1,
            u'два': 2,
            u'две': 2,
            u'три': 3, 
            u'четыре': 4,
            u'пять': 5,
            u'шесть': 6,
            u'семь': 7,
            u'восемь': 8,
            u'девять': 9
        }
        tens = {
            u'десять': 10,
            u'одиннадцать': 11,
            u'двенадцать': 12,
            u'тринадцать': 13,
            u'четырнадцать': 14,
            u'пятнадцать': 15,
            u'шестнадцать': 16,
            u'семнадцать': 17,
            u'восемнадцать': 18,
            u'девятнадцать': 19,
            u'двадцать': 20,
            u'тридцать': 30,
            u'сорок': 40,
            u'пятьдесят': 50,
            u'шестьдесят': 60,
            u'семьдесят': 70,
            u'восемьдесят': 80,
            u'девяносто': 90
        }
        hundreds = {
            u'сто': 100,
            u'двести': 200,
            u'триста': 300,
            u'четыреста': 400,
            u'пятьсот': 500,
            u'шестьсот': 600,
            u'семьсот': 700,
            u'восемьсот': 800,
            u'девятьсот': 900
        }

        numwords = {}
        for word, idx in units.items(): numwords[word] = idx
        for word, idx in tens.items(): numwords[word] = idx
        for word, idx  in hundreds.items(): numwords[word] = idx

        result = 0

        for word in num.split():
            result += numwords[word]

        return result

def calc(string):
    result = 0
    if '*' in string:
        words = [s.strip() for s in string.split('*')]
        result = Number(words[0]) * Number(words[1])
    elif '+' in string:
        words = [s.strip() for s in string.split('+')]
        result = Number(words[0]) + Number(words[1])
    elif '-' in string:
        words = [s.strip() for s in string.split('-')]
        result = Number(words[0]) - Number(words[1])
    else:
        words = [s.strip() for s in string.split('/')]
        result = Number(words[0]) / Number(words[1])
    return result

string = 'пятьдесят пять / один'

print(calc(string))

r = requests.get('https://weird-math.yactf.ru', verify=False)

while True:
    print('=============================')
    json = r.json()
    print(json)
    token = r.headers['X-Weird-Math-Token']
    print(token)

    task = json[list(filter(lambda x: x != 'Tip' and x != 'Message', json.keys()))[0]]
    answer = calc(task)
    print('{} = {}'.format(task, answer))

    r = requests.post('https://weird-math.yactf.ru', verify=False, json=answer.get_num(), headers={'X-Weird-Math-Token': token})



# print(Number('0b10011110').num)
# print(Number('0o1477').num)
# print(Number('eight hundred forty six').num)
# print(Number('four hundred thirty nine').num)
# print(Number('MDCCLXXVI').num)
# print(Number('MCMLIV').num)
# print(Number('MMXIV').num)