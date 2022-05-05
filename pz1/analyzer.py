import pymorphy2


class AnalyzeHandler:
    _analyzer = pymorphy2.MorphAnalyzer()
    _cases = {"nomn": "Именительный", "gent": "Родительный", "datv": "Дательный",
              "accs": "Винительный", "ablt": "Творительный", "loct": "Предложный"}

    def analyze(self, words):
        for word in words:
            analysis = self._analyzer.parse(word)[0]

            word_cases = []
            word_cases_plural = []
            for case in self._cases.keys():
                word_cases.append(analysis.inflect({case}).word)
                word_cases_plural.append(analysis.inflect({'plur', case}).word)

            print(f"{words.index(word) + 1} Морфологический разбор слова \"{word}\" ")
            print("Начальная форма:            " + analysis.normal_form)
            print("Морфологические признаки:   " + analysis.tag.cyr_repr)

            table_header = "\n" + "Падеж" + " " * 14 + "Единственное число" + " " * 5 + "Множественное число"
            print(table_header)

            case_max_len = max(len(case) for case in self._cases.values())

            spaces = []
            for case in self._cases.values():
                spaces.append(case_max_len - len(case) + 6)

            strings = []
            i = 0
            for case in self._cases.values():
                strings.append(case + ":" + " " * spaces[i])
                i += 1

            spaces = []
            i = 0
            for word_case in word_cases:
                spaces.append(len(table_header) - len(word_case) - len("Множественное число") - len(strings[i]) - 1)
                i += 1

            for i in range(len(strings)):
                strings[i] += word_cases[i] + " " * spaces[i] + word_cases_plural[i]

            for string in strings:
                print(string)

            print()
            print("--------------------------------------------------------------")
            print()


if __name__ == '__main__':
    handler = AnalyzeHandler()
    handler.analyze(["компьютер", "машина", "ноутбук", "планшет", "сети", "техника", "офис", "мультимедиастанция",
                     "бухгалтерия", "процессор", "драйвер", "видеоигра"])
