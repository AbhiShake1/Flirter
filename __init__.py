import json
import random
from text_to_speech import TextToSpeech as tts

engine: tts = tts()


def get_nickname():
    def ask_nickname():
        engine.say("You can call be anything babe i am all yours. I will remember my nickname")
        with open("files/name.txt", "w") as file:
            name = engine.listen()
            while "sober" in name:
                name = engine.listen()
                file.write(engine.listen())
        engine.say("That is a nice name. I will never forget that")

    try:
        with open("files/name.txt") as f:
            nick_name = f.read()
            if not nick_name.strip():
                ask_nickname()
            else:
                engine.say(f"My name given by my sweetheart is {nick_name}")
    except FileNotFoundError:
        ask_nickname()


def get_commands():
    while True:
        # read from terminal without input message
        command = engine.listen().lower()
        with open("files/keywords.json") as JSon:
            data: dict = json.loads(JSon.read())

        entered: bool = False
        # iterating through the parsed dictionary/map
        for keyword, messages in data.items():
            if keyword in command:
                entered = True
                if isinstance(messages, list):
                    engine.say(random.choice(messages))
                elif isinstance(messages, str):
                    engine.say(messages)
            elif "your name" in command:
                entered = True
                get_nickname()
            elif "bye" in command or "quit" in command or "fuck off" in command:
                entered = True
                engine.say("It was a pleasure talking to you. Hope we can hang out soon")
                break
        if not entered:
            engine.say("Sorry, could you tell that again please? You sound like you are heavily drunk")


if __name__ == '__main__':
    engine.greet()

    get_commands()
