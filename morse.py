from pynput.keyboard import Key, Controller
import time
import argparse
keyboard = Controller()


def get_letter(letter):
    m = open("morse.txt", "r")
    for line in m:
        (key, val) = line.split()
        if letter.lower() == str(key):
            return str(val)
def execute(message, **kwargs):
    morse = ""
    for letter in message: 
        if letter != " ":
            morse = morse + get_letter(letter) + "\n"
            for char in get_letter(letter):
                if char == "-":
                    keyboard.press(Key.space)
                    time.sleep(0.24)
                    keyboard.release(Key.space)
                elif char == ".":
                    keyboard.press(Key.space)
                    time.sleep(0.08)
                    keyboard.release(Key.space)
            time.sleep(0.3)
        else:
            morse += " \n"
            time.sleep(0.7)


parser = argparse.ArgumentParser(
    description="Send a message in morse")
parser.add_argument(
    'message',
    type=str,
    help="Enter a message"
)
args = parser.parse_args()
time.sleep(3)
execute(args.message)