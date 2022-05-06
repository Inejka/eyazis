import os

from nltk.draw import TreeWidget
from nltk.draw.util import CanvasFrame
import nltk
from nltk.corpus import wordnet as wn
from PIL import Image, ImageDraw


def analyse(text):
    text = text.replace('\n', '')
    text = text.replace(',', '')
    text = text.replace('.', '')

    if text == "":
        return

    canvas = CanvasFrame()

    tokens = nltk.word_tokenize(text)
    result = '(S '
    result_sent = '(SENT '
    for token in tokens:
        result_sent += get_word_semantic(token)
    result_sent += ')'
    result += result_sent
    result += ')'

    widget = TreeWidget(canvas.canvas(), nltk.tree.Tree.fromstring(result))
    canvas.add_widget(widget, 50, 10)
    canvas.print_to_file("test.ps")
    img = canvas_to_image(canvas)
    img.show()


def get_word_semantic(word):
    filename = word

    dictionary = {}
    if len(wn.synsets(word)) == 0:
        return '(WS (W ' + word + '))'
    dictionary['W'] = word
    result = '(WS (W ' + word + ') (DEF ' + \
             wn.synsets(word)[0].definition().replace(' ', '_') + ')'
    dictionary['DEF'] = wn.synsets(word)[0].definition().replace(' ', '_')
    synonyms, antonyms, hyponyms, hypernyms = [], [], [], []
    word = wn.synsets(word)
    syn_app = synonyms.append
    ant_app = antonyms.append
    he_app = hyponyms.append
    hy_app = hypernyms.append
    for synset in word:
        for lemma in synset.lemmas():
            syn_app(lemma.name())
            if lemma.antonyms():
                ant_app(lemma.antonyms()[0].name())
    for hyponym in word[0].hyponyms():
        he_app(hyponym.name())
    for hypernym in word[0].hypernyms():
        hy_app(hypernym.name())
    if len(synonyms):
        result += ' (SYN '
        synDictionary = []
        for synonym in synonyms:
            synDictionary.append(synonym)
            result += synonym + ' '

        dictionary['SYN'] = synDictionary
    if len(antonyms):
        result += ') (ANT '
        antDictionary = []
        for antonym in antonyms:
            antDictionary.append(antonym)
            result += antonym + ' '

        dictionary['ANT'] = antDictionary
    if len(hyponyms):
        result += ') (HY '
        hypoDictionary = []
        for hyponym in hyponyms:
            hypoDictionary.append(hyponym)
            result += hyponym + ' '

        dictionary['HY'] = hypoDictionary
    if len(hypernyms):
        result += ') (HE '
        hypeDictionary = []
        for hypernym in hypernyms:
            hypeDictionary.append(hypernym)
            result += hypernym + ' '

        dictionary['HE'] = hypeDictionary
    result += '))'

    # with open(filename + '.json', 'w') as json_file:
    #    json.dump(dictionary, json_file, indent=4, sort_keys=True)
    return result


def canvas_to_image(canvas):
    filename = 'tree.ps'

    canvas.print_to_file(filename)

    with open(filename, 'r') as file:
        filedata = file.read()

    filedata = filedata.replace(',', '.')

    with open(filename, 'w') as file:
        file.write(filedata)

    img = Image.open(filename)
    os.remove(filename)
    return img
