import re

class LexicalParser:
    rules = []

    def __init__(self, rules):
        self.rules = [{'re': re.compile('^' + x['re']), 'type': x['type']} for x in rules]

    def create_token(self, type, value):
        return {
            'type': type,
            'value': value
        }

    def parse(self, string, skip_spaces=True):
        current = string
        result = []

        while len(current) != 0:
            rule_applied = False
            if skip_spaces:
                current = current.strip()
            for rule in self.rules:
                match = rule['re'].match(current)
                if match:
                    result.append(self.create_token(rule['type'], match.group(0)))
                    current = current[match.end(0):]
                    rule_applied = True

            if not rule_applied:
                symbol = current[0]
                result.append(self.create_token('UNDEFINED', symbol))
                current = current[1:]

        return result

class Rule:
    context_re = ''

    def __init__(self, context_re):
        self.context_re = re.compile(context_re)

    def reduce(self, stack, context):
        if self.context_re.match(context):
            pass

class Parser:
    stack = ''
    rules = []

    # check reduce rules here
    def __init__(self, rules):
        self.rules = rules

    def shift(self, string):
        pass
    
    def reduce(self, stack, next):
        result = stack
        changed = True

        while changed:
            changed = False

            for rule in self.rules:
                if result.endswith(rule['in']):
                    result = result[:-len(rule['in'])] + rule['out']
                    self.applied.append(rule)
                    changed = True
                    break

        return result

    def error(self):
        pass

    def parse(self, string, skip_spaces=True):
        self.applied = []

        stack = []

        for letter in string:
            if skip_spaces and letter == ' ':
                continue
            stack = self.reduce(stack, letter)

        return (stack, self.applied)


# parser = Parser([{
#         'in': 'E*B',
#         'out': 'E'
#     }, {
#         'in': 'E+B',
#         'out': 'E'
#     }, {
#         'in': 'B',
#         'out': 'E'
#     }, {
#         'in': '0',
#         'out': 'B'
#     }, {
#         'in': '1',
#         'out': 'B'
#     }])

# lexic = LexicalParser([{
#     're': r'*',
#     'type': 'MUL'
# }, {
#     're': r'[+\-*/]',
#     'type': 'OPERATOR'
# }, {
#     're': r'[0-9]+',
#     'type': 'NUM'
# }])

# tokens = lexic.parse('1111 + 122 * 224 - 123')

# print(tokens)

parser = Parser([
    # DIGIT = [0..9]
    Rule(r'.*', [{
        'type': 'SYMBOL',
        'value': r'.*'
    }], [{
        'type': 'DIGIT'
    }]),
    Rule(r'.*') # NUM = DIGIT | NUM DIGIT
])

answer = parser.parse('1 + 1')

print(answer)