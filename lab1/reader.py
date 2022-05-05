from striprtf.striprtf import rtf_to_text


class Reader:
    @staticmethod
    def read(path):
        with open(path) as file:
            string = "\n".join(file.readlines())
            if path.endswith('.txt'):
                return string
            if path.endswith('.rtf'):
                return rtf_to_text(string)
