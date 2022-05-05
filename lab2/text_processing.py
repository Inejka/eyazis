from nltk.draw import TreeWidget
from nltk.draw.util import CanvasFrame
import nltk
grammar = """
            P: {<PRT|ADP>}
            V: {<VERB>}
            N: {<NOUN|PRON>}
            NP: {<N|NP|P>+<ADJ|NUM|DET>+}
            NP: {<ADJ|NUM|DET>+<N|NP|P>+}
            PP: {<P><NP>|<NP><P>}
            VP: {<NP|N><V>}
            VP: {<VP><NP|N||ADV>}
            VP: {<NP|N|ADV><VP>}
            VP: {<VP><PP|P>}
            """

def analyse(text):
    text = text.replace('\n', '')
    text = text.replace(',', '')

    if text == "":
        return

    canvas = CanvasFrame()
    substr = text
    j = 0

    while True:
        i = substr.find('.')
        if i == -1:
            break
        else:
            tmp = substr[:i]
        tokens = nltk.word_tokenize(tmp)
        tokens = nltk.pos_tag(tokens, tagset='universal')
        parser = nltk.RegexpParser(grammar)
        tree = parser.parse(tokens)

        widget = TreeWidget(canvas.canvas(), tree)
        canvas.add_widget(widget, 250, j + 10)
        j += 200
        substr = substr[i + 1:]
    tree.draw()




