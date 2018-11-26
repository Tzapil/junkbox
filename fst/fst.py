   
import re
from graphviz import Digraph

class FST:
    def __init__(self, file_name):
        # можно просто переменную-счетчик. не нужно использовать set
        self.states = 0
        self.final_states = set()
        self.delta = {}
        # Sigma, Delta не используются
        self.file_to_fst(file_name)

    def add_transition(self, from_state, inputsymbol, outputsymbol):
        next_from_state = self.new_state()
        self.delta[(from_state, inputsymbol)] = {(next_from_state, outputsymbol)}
        return next_from_state

    def append_transition(self, from_state, inputsymbol, outputsymbol):
        next_from_state = self.new_state()
        self.delta[(from_state, inputsymbol)].add((next_from_state, outputsymbol))
        return next_from_state

    def new_state(self):
        self.states += 1
        return self.states

    # тут скорее add_to_final
    def add_final(self, state):
        self.final_states.add(state)

    def file_to_fst(self, file_name):
        # with open(file_name) as file:
        with open(file_name, encoding='utf-8-sig') as file:
            for line in file:
                field = re.sub(r'[:.\[\]]|(\w*=)', '', line.strip()).split()
                output = field[1:] # field[1:] не даст тот же результат?
                input = list(field[0]) + ['eps'] * (len(output) - len(field[0])) # ['г', 'л', 'а', 'г', 'о', 'л'] + ['eps'] * (количество элементов аутпут - длинна глагола) ???
                self.make_path(output, input)

    def make_path(self, output, input):
        # next_from_state не используется
        from_state = 0
        for i in range(len(output)):
            # суперсложные условия
            # не разберешь без комментариев
            # лучше заранее в переменные с понятными названиями положить или определить функции для вычисления
            current_state = (from_state, input[i])
            if current_state in self.delta.keys():
                if output[i] in [pair[1] for pair in self.delta[(from_state, input[i])]]:
                    from_state = [paar[0] for paar in self.delta[(from_state, input[i])] if paar[1] == output[i]].pop()
                else:
                    from_state = self.append_transition(from_state, input[i], output[i])    
            else:
                from_state = self.add_transition(from_state, input[i], output[i])
        self.add_final(from_state) # проверка странная выглядит ненужной

    def draw(self):
        fst = Digraph('Finite State Transducer')
        fst.attr(rankdir='LR', size='8,5', shape='circle')
        fst.attr('node', shape='circle')
        for key in sorted(self.delta.keys(), key=lambda paar: paar[0]):
            for pair in self.delta[key]:
                if pair[0] in self.final_states:
                    fst.node(str(pair[0]), shape='doublecircle')
                fst.edge(str(key[0]), str(pair[0]), label=key[1] + ':' + pair[1])
        fst.render('./fst.gv', view=True)

    def rec_lookup(self, state, visited, path, symbol, symbol_list, outputs, final_result):
        visited.append(state)
        path.append(state)
        if state in self.final_states:
            a_copy = outputs.copy()
            final_result.append(a_copy)
        else:
            if (state, symbol) not in self.delta.keys():
                return
            lst = list(self.delta[(state, symbol)])
            for pair in lst:
                if pair[0] not in visited:
                    outputs.append(pair[1])
                    self.rec_lookup(pair[0], visited, path, symbol_list[len(outputs)], symbol_list, outputs, final_result)
        path.pop()
        if outputs:
            outputs.pop()
        visited.remove(state)

    def lookup(self, word):
        word_list = list(word) + ['eps'] * 20
        visited = []
        path = []
        outputs = []
        final_result = []
        self.rec_lookup(0, visited, path, word_list[0], word_list, outputs, final_result)
        return final_result


f = FST('./werfen.txt')
f.draw()
verbs = ['geworfen', 'warfen', 'warfst', 'warft', 'warf', 'werfend', 'werfen', 'werfest',
         'werfet', 'werfe', 'werft', 'wirfst', 'wirf', 'würfen', 'würfest',
         'würfet', 'würfe', 'würfst']
for verb in verbs:
    print(verb)
    for i in f.lookup(verb):
        print(i)
    print()
