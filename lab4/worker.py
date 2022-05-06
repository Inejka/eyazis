import pickle
import spacy

from bs4 import BeautifulSoup
import requests


class Worker():
    def __init__(self):
        import os
        self.nlp = spacy.load('ru_core_news_lg')
        self.url = "https://knigopoisk.org/search?bookName=&author="
        self.data = {}
        self.transfer = {}
        for name in os.listdir('obj'):
            type_name = name[:name.find('_')]
            to_add = self.load_obj(name)
            if "number" in name:
                self.transfer[type_name] = to_add
            else:
                self.data[type_name] = to_add

    def all_in(self, to_find, to_search):
        for word in self.nlp(to_find):
            if word.lemma_ not in to_search: return False
        return True

    def save_obj(self, obj, name):
        with open('obj/' + name, 'wb') as f:
            pickle.dump(obj, f, pickle.HIGHEST_PROTOCOL)

    def load_obj(self, name):
        with open('obj/' + name, 'rb') as f:
            return pickle.load(f)

    def process_tags(self, string):
        url_gen = {}
        for key, value in self.data.items():
            url_gen[key] = "&" + key + "=@"
        for sent in string.split(','):
            for key, value in self.data.items():
                sentance = None
                for big_sent in value:
                    if self.all_in(sent, big_sent):
                        sentance = big_sent
                        break
                if sentance is not None:
                    if url_gen[key].endswith("@"):
                        url_gen[key] = url_gen[key].replace('@', self.transfer[key][sentance])
                    else:
                        url_gen[key] += "%2C" + self.transfer[key][sentance]
        return url_gen

    def gen_url(self, url_gen):
        tmp = self.url
        for _, value in url_gen.items():
            value = value.replace('@', '')
        tmp += url_gen['genre']
        tmp += url_gen['ageReader']
        tmp += url_gen['scene']
        tmp += url_gen['plotMoves']
        tmp += url_gen['lifetime']
        tmp += url_gen['linearityPlot']
        tmp += url_gen['feature']
        tmp += "&yt0=Поиск"
        return tmp

    def gen_names(self, string):
        print(string)
        url = self.gen_url(self.process_tags(string))
        print(url)
        names = []
        search_results = BeautifulSoup(requests.get(url).text, 'html.parser').select(".search-result")[0]
        for i in search_results.find_all('img'):
            names.append(i.attrs['alt'])
            if len(names) == 4:
                return names
        return names


if __name__ == "__main__":
    worker = Worker()
    print(worker.gen_names("мистика, драконы, развод"))
