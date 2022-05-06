def collect_dicts():
    features_to_number = {}
    features_dict = []
    bs = BeautifulSoup(requests.get(url).text, "html.parser").select("#features-tog > ul:nth-child(1)")
    for i in bs[0]:
        features_to_number[re.sub(r"\B([А-Я])", r" \1", i.text)] = i.input.attrs['value']
        features_dict.append(re.sub(r"\B([А-Я])", r" \1", i.text))
    save_obj(features_to_number, "features_to_number")
    save_obj(features_dict, "features_dict")


def lemma_dicts():
    import os

    print(os.listdir('obj'))
    for name in os.listdir('obj'):
        if "number" in name:
            to_save = {}
            dct = load_obj(name)
            print(dct)
            for key, value in dct.items():
                new_key = ""
                for token in nlp(key):
                    new_key += token.lemma_ + ' '
                to_save[new_key] = value
            print(to_save)
            print("---------------------------------------------------------------------------------")
            save_obj(to_save, name)
        else:
            lst = load_obj(name)
            print(lst)
            to_save = []
            for sent in lst:
                new_sent = ""
                for token in nlp(sent):
                    new_sent += token.lemma_ + ' '
                to_save.append(new_sent)
            print(to_save)
            print("---------------------------------------------------------------------------------")
            save_obj(to_save, name)

# https://melaniewalsh.github.io/Intro-Cultural-Analytics/05-Text-Analysis/Multilingual/Russian/01-Preprocessing-Russian.html
url = "https://knigopoisk.org/search"