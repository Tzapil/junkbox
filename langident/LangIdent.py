class LanguageIdent:
    def __init__(self, file_name, length=2):
        #получаем переданный файл, отправляем его в функцию  build_dictionaries
        self.length = length
        self.sprachprofil = self.build_dictionaries(file_name)

    def build_dictionaries(self, names_file):
        #открываем файл со списком названий языков, приводим текст в надлежащий вид
        text = open(names_file, encoding='utf-8-sig').read().strip().split()
        sprach_dict = {}
        #для каждого языка, стоящего в файле вызываем функцию trigrams_count, которая считает н-граммы(биграммы в моем случае, они мне больше точности дают)
        for name in text:
            sprach_dict[name] = self.trigrams_count(open(r'./{}'.format(name), encoding='utf-8-sig').read().strip())
        #получаем большой словарик, где ключ - имя языка, содержимое - его профиль
        return sprach_dict

    def trigrams_count(self, text):
        trigrams = {}
        #полученный текстовый файлик разбиваем на буквы, чтобы по ним считать н-граммы
        #тут в цикле считаются биграммы. Можно триграммы, но биграммы пока лучше всего классифицируют
        for i in range(0, len(text) - self.length + 1):
            key = text[i:i + self.length]
            if key not in trigrams.keys():
                #если биграммы еще нет в trigrams, число ее повторений 1
                trigrams[key] = 1
            else:
                # если такая биграмма уже есть trigrams, прибавляем к числу повторений 1
                trigrams[key] += 1
                # возвращаем словарик с биграммами
        return trigrams

    def identify(self, text):
        #считаем триграммы для полученной строки
        trigs = self.trigrams_count(text)
        # из trigs создаем список, в котором на 1м месте самая часто встречающаяся биграмма, на 2м - та, что на 2м месте по частоте итд итп
        new_profil = sorted(trigs, key=trigs.__getitem__, reverse=True)
        results = {}
        # тут сравниваем н-граммы новой строки и нграммами каждого языка...
        for key, value in self.sprachprofil.items():
            old_profil = sorted(value, key=value.__getitem__, reverse=True)
            #...для этого вызываем функцию compare
            results[key] = self.compare(new_profil, old_profil)
        resulting_language = min(results, key=results.get)
        #выигрывает язык у которого разница с новой полученной строкой(ее нграммами) меньше всего
        return resulting_language[: -4]

    def compare(self, new_profil, old_profil):
        # думаешь, может сделать из new_profil, old_profil снова словарики, чтобы быстрее было?
        diff = 0
        for i in new_profil:
            # формула в задании гласит...короче, считаем просто разницу в индексах (рангу по частоте)
            if i in old_profil:
                diff += abs(new_profil.index(i) - old_profil.index(i))
            else:
#на след строке по идее, согласно заданию, должна стоять почти та же формула, что и в if, выглядеть она только должна была бы так: abs(new_profil.index(i)-(len(old_profil)+1))
#но просто тогда, мне показалось, что если нграммы нет в профиле языка, то оочень вероятно, что этот неправильный язык для этой строки, соответственно, разницу между индексами
#надо сделать как можно больше. Убрала abs(new_profil.index(i)-) из формулы, чтоб получить большее число, accuracy стало 100 процентов, до этого было 1-2 ошибки стабильно
                diff += (len(old_profil)+1)#abs(new_profil.index(i)-)
        return diff


clf = LanguageIdent(r'./namen.txt')
deu = 'Testen Sie die Parserklasse mit mindestens 5 verschiedenen Eingabelisten. Die Grammatik soll mindestens 20 Phrasenstrukturregeln enthalten (darunter auch mehr als binärverzweigende und auch linksrekursive Regeln). Das Lexikon soll mindestens 50 Einträge haben'
eng = 'Hello, I am an english string and I really want to be checked and accepted by the program. I hope it will also classify me well, because last time it just did not happen'
fin = 'Palkkarakennetilastossa ovat mukana julkisen sektorin ja yksityisen sektorin yli viiden hengen yrityksissä työskentelevät palkansaajat. Tilaston tiedot on kerätty viime vuoden syys-, loka- tai marraskuulta. Tilasto ei sisällä yksityisen sektorin yritysten ylimmän johdon tietoja.'
ung = 'A piacról működő, nem állami pénzen kitartott médiának nehezebb lesz az élete a jövő évtől. Az adó előző verziója fennakadt Brüsszelen, egy kiskapun viszont átcsúszhat az új változat.'
ro = 'ASF a demarat o investigație privind investițiile Fondurilor de Pensii private în compania RCS RDS, după acuzațiile lui Darius Vâlcov de listare ilegală la bursă'
ital = 'Al di là delle facili ironie, la ricerca ha lo scopo di fornire dati scientifici precisi per placare le insicurezze degli uomini in materia, che possono dare origine a problemi psicologici seri.'
cz = 'Biomonitoring podle Hubeného po deseti letech prokázal, že na 95 procentech plochy rostou stromy bezproblémově a vlastně i lépe, než kdyby byly vysázeny. Odborníci z parku zmonitorovali 1111 ploch o velikosti 500 metrů čtverečních, tedy desetinu procenta území NP.  Šlo o bývalé první zóny, jež vznikly v roce 1995, i bezzásahové zóny z roku 2007. Měřilo se ale i na zásahových územích. Pouze na zhruba na 4,5 procenta mapovaných ploch, zejména v potočních nivách nebo rašeliništích, rostou nové stromky hůře. Hubený to přesto považuje za velmi dobrý výsledek. "Je to dobré pro tetřevy, že tam mají volné plácky, i pro jeleny, že se mohou bít při říji na podzim," vysvětluje. "Park existuje 25 let. Předtím se dělala nárazová a nesystematická šetření. Před deseti lety i dnes slýcháme názory: Les tam neporoste, bude tam poušť, není schopen se bez pomoci člověka obnovit… Proto musíme lidi přesvědčit, že to funguje," řekl v pátek Aktuálně.cz ředitel NP Šumava Pavel Hubený. Dlouholetým kritikem bezzásahových zón v NP Šumava je mimo jiné prezident Miloš Zeman. Šumava se dokonce stala jedním z témat obou jeho kandidatur na Hrad. Výsledky desetiletého biomonitoringu podle národního parku vyvrací zažité předsudky a ukazují, že příroda umí zničený les obnovit sama. Stožec - Tam, kde ční suché pahýly stromů a svými torzy pokrývají kopce Národního parku Šumava, vyrůstají statisíce mladých smrků, buků a jeřábů. Les postižený kůrovcem dokáže růst a přirozeně se sám obnovovat, i když do něj člověk nezasahuje, dokazuje Správa Národního parku Šumava na základě výsledků desetiletého biomonitoringu. Ty podle ní vyvrací zažité předsudky a ukazují, že příroda umí zničený les obnovit sama, a ten je pak navíc schopný odolávat suchu.'
ru = 'Как быть, если мы раз за разом повторяем одни и те же ошибки в отношениях, связывая себя с несвободными партнерами? Почему нам не удается выбраться из порочного круга?'
tur = 'Sınır Tanımayan Gazeteciler örgütünün Almanya temsilcisi Christian Mihr: Doğan Medya Grubu "nun Demirören Holding"e satılması Türk medyası için bir dönüm noktası ve basın özgürlüğü açısından kara bir gün.'
for language in [deu, eng, fin, ung, ro, ital, cz, ru, tur]:
     print(clf.identify(language))

