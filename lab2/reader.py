import textract


class Reader:
    @staticmethod
    def read(path):
        if path.endswith('.doc'):
            return textract.process(path).decode("utf-8")
