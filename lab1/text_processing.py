# -*- coding: utf-8 -*-

import nltk

from pymorphy2 import MorphAnalyzer
from pymorphy2.tagset import OpencorporaTag
from enum import Enum

part_of_sentence = {
    'subject': 'NOUN nomn,NPRO',
    'predicate': 'VERB',
    'definition': 'ADJF,ADJS,NUMR',
    'addition': 'NOUN,NPRO',
    'circumstance': 'INFN,ADVB,GRND,PRTF,PRTS',
}

nltk.download('punkt')
# основное хранилище данных
main_dictionary = []


class RuPartOfSent(Enum):
    SUBJECT = 'Подлежащее'
    PREDICATE = 'Сказуемое'
    DEFINITION = 'Определение'
    ADDITION = 'Дополнение'
    CIRCUMSTANCE = 'Обстоятельство'
    UNKNOWN = ''


class Lexeme:
    lexeme = ''
    tags = ''
    part_of_sent = ''

    def __eq__(self, other):
        return True if self.lexeme.lower() == other.lexeme.lower() and self.tags.lower() == other.tags.lower() and \
                       self.part_of_sent.lower() == other.part_of_sent.lower() else False

    def __ne__(self, other):
        return True if self.lexeme.lower() != other.lexeme.lower() and self.tags.lower() != other.tags.lower() and \
                       self.part_of_sent.lower() != other.part_of_sent.lower() else False

    def __gt__(self, other):
        return True if self.lexeme.lower() > other.lexeme.lower() else False

    def __ge__(self, other):
        return True if self.lexeme.lower() >= other.lexeme.lower() else False

    def __lt__(self, other):
        return True if self.lexeme.lower() < other.lexeme.lower() else False

    def __le__(self, other):
        return True if self.lexeme.lower() <= other.lexeme.lower() else False

    def __getitem__(self, vals):
        if vals == 0:
            return self.lexeme
        if vals == 1:
            return self.tags
        if vals == 2:
            return self.part_of_sent
        return None


def get_words_from_text(text: str) -> list:
    sentences = nltk.sent_tokenize(text)
    words = []
    for sentence in sentences:
        for word in nltk.word_tokenize(sentence):
            if word != '.' and word != ',' and word != '?' and word != '!':
                words.append(word.lower())
    return words


def get_part_of_sent(tags: OpencorporaTag, has_subject: bool) -> RuPartOfSent:
    if tags.POS == 'NOUN' and tags.case == 'nomn':
        return RuPartOfSent.SUBJECT
    elif tags.POS == 'NOUN':
        return RuPartOfSent.ADDITION
    elif tags.POS == 'NPRO' and has_subject:
        return RuPartOfSent.ADDITION
    elif tags.POS == 'NPRO':
        return RuPartOfSent.SUBJECT
    for i in part_of_sentence.items():
        if tags.POS in i[1]:
            return RuPartOfSent[i[0].upper()]
    return RuPartOfSent.UNKNOWN


def get_lexemes_from_text(text: str) -> list:
    lexemes = []
    words = get_words_from_text(text)
    morph = MorphAnalyzer()
    has_subject = False
    for word in words:
        le = morph.parse(word)[0]
        lexeme = Lexeme()
        lexeme.lexeme = word
        lexeme.tags = le.tag.cyr_repr
        lexeme.part_of_sent = get_part_of_sent(le.tag, has_subject).value
        if lexeme.part_of_sent == 'Подлежащее':
            has_subject = True
        lexemes.append(lexeme)
    return lexemes


def parser(string: str):
    misc_symbols = ['.', ',', '!', '?', ':', ';', '(', ')', '«', '»', '—', '…']
    for i in misc_symbols:
        string = string.replace(i, '')
    lexemes = get_lexemes_from_text(string)
    lexemes.sort()

    for lex in lexemes:
        add_flag = True
        for j in main_dictionary:
            if lex == j:
                add_flag = False
        if add_flag:
            main_dictionary.append(lex)
