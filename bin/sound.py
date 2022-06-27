import gtts

class Sound:

    def __init__(self, text):
        self.text = text

    def encode_to_mp3(self, filename, path):
        sound = gtts.gTTS(self.text)
        sound.save(path + "/" + filename + ".mp3")
