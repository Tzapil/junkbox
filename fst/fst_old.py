
import re
from graphviz import Digraph

class FST:
     def __init__(self, file_name):
         self.start_state = 0       # нинужна
         self.states = {0}          # сет не нужен, можно просто число хранить
         self.Sigma = set()         # нинужна
         self.Delta = set()         # нинужна
         self.final_states = set()  
         self.delta = {}
         self.file_to_fst(file_name)

     # я бы разбил на 2 функции add_transition и append_transition
     # а проверку в make_path делал.
     def add_transition(self, from_state, inputsymbol, outputsymbol):
             next_from_state = 0
             if ((from_state, inputsymbol) not in self.delta.keys()):
                 next_from_state = self.new_state()
                 self.delta[(from_state, inputsymbol)] = {(next_from_state, outputsymbol)}
             elif ((from_state, inputsymbol) in self.delta.keys() and outputsymbol not in [pair[1] for pair in self.delta[(from_state, inputsymbol)]]):
                 next_from_state = self.new_state()
                 self.delta[(from_state, inputsymbol)].add((next_from_state, outputsymbol))
             return next_from_state

     # со счетчиком проще
     # new = self.last_index + 1
     # return self.last_index
     def new_state(self):
         new = max(self.states) + 1
         self.states.add(new)
         return new

     # по логике название должно быть что то типа def add_to_final(self, state):
     # тк просто добавляем в сет, а не создаем ничего и даже не возвращаем
     def make_final(self, state):
         self.final_states.add(state)
         return # пустой ретурн

     def file_to_fst(self, file_name):
         # with open(file_name, encoding='utf-8-sig') as file:
         file = open(file_name, encoding='utf-8-sig')
         for line in file:
            field = re.sub(r'[(:.)(\[)(\])]|(\w*=)', '', line.strip()).split()
            output = list(field[1]) + field[2:]
            input = list(field[0]) + ['eps'] * (len(output) - len(field[0]))
            self.make_path(output, input)
            self.Sigma.update(set(input))  # нинужно
            self.Delta.update(set(output)) # нинужно
         return # пустой ретурн

     def make_path(self, output, input):
         next_from_state = 0 # бесполезная переменная
         from_state = self.start_state # = 0
         for i in range(len(output)):
             # суперсложные условия. я бы разбил попроще
             if (from_state, input[i]) in self.delta.keys() and output[i] in [pair[1] for pair in self.delta[(from_state, input[i])]]:
                 # from_state =
                 next_from_state = [paar[0] for paar in self.delta[(from_state, input[i])] if paar[1] == output[i]].pop()
             else:
                 # from_state = 
                 next_from_state = self.add_transition(from_state, input[i], output[i])
             # можно после цикла сделать один раз. такая проверка в цикле выглядит странно)
             if i == len(output) - 1:
                 self.make_final(next_from_state)
                 return
             # удаляем
             from_state = next_from_state

     def draw(self):
         fst = Digraph('Finite State Transducer')
         fst.attr(rankdir='LR', size='8,5')
         for key in sorted(self.delta.keys(), key=lambda paar: paar[0]):
             for pair in self.delta[key]:
                if pair[0] in self.final_states:
                    fst.attr('node', shape='doublecircle')
                    fst.node(str(pair[0]))
                # я бы как нибудь так написал
                # shape = 'circle'
                # if pair[0] in self.final_states:
                #     shape = 'doublecircle'
                # fst.attr('node', shape=shape)
                fst.attr('node', shape='circle')
                fst.edge(str(key[0]), str(pair[0]), label=key[1] + ':' + pair[1])
         fst.render(r'./fst.gv', view=True)
         return # пустые ретурны (

     def rec_lookup(self, state, visited, path, symbol, symbol_list, outputs, final_result):
         visited.append(state)
         path.append(state) # path не используется нигде
         if state in self.final_states:
             a_copy = outputs.copy()
             final_result.append(a_copy)
         else:
             # кажется эту проверку можно самой первой делать
             if (state, symbol) not in self.delta.keys():
                 return
             # list(self.delta[(state, symbol)]) лучше сделать здесь до цикла. чтобы каждый раз не кастовать
             # так и обходить будет проще без range)
             for i in range(len(self.delta[(state, symbol)])):
                 pair = list(self.delta[(state, symbol)])[i]
                 if pair[0] not in visited:
                     outputs.append(pair[1])
                     self.rec_lookup(pair[0], visited, path, symbol_list[len(outputs)], symbol_list, outputs, final_result)
         path.pop()
         if outputs:
             outputs.pop()
         visited.remove(state)

     def lookup(self, word):
         # волшебные числа ((
         word_list = list(word) + ['eps'] * 20
         visited = []
         path = []
         outputs = []
         final_result = []
         self.rec_lookup(self.start_state, visited, path, word_list[0], word_list, outputs, final_result)
         return final_result


f = FST(r'./werfen.txt')
f.draw()
print(f.delta)
verbs = ['geworfen', 'warfen', 'warfst', 'warft', 'warf', 'werfend', 'werfen', 'werfest',
         'werfet', 'werfe', 'werft', 'wirfst', 'wirf', 'würfen', 'würfest',
         'würfet', 'würfe', 'würfst']
for verb in verbs:
    print(verb)
    for i in f.lookup(verb):
        print(i)
    print()

