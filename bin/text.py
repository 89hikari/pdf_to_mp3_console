import textract

class Text:

    def __init__(self, text_url):
        self.text_url = text_url

    def text_decode(self):
        try:
            return textract.process(self.text_url).decode()
        except textract.exceptions.MissingFileError:
            return False
