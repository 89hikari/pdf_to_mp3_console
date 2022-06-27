import sys
from bin.text import Text
from bin.sound import Sound

def run():
    text = Text(input("Path to file > "))

    while text.text_decode() == False:
        text = Text(input("File not found. Try again > "))

    decoded_text = text.text_decode()
    
    sound = Sound(decoded_text)

    filename = input("Enter the name of .mp3 file > ")
    save_directory = input("Enter directory for the file saving > ")

    print("Processing...")

    sound.encode_to_mp3(filename, save_directory)
    
run()
