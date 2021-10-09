from text_to_speech import TextToSpeech as tts
import random

engine: tts = tts()


def get_nickname():
    def ask_nickname():
        engine.say("You can call be anything babe i am all yours. I will remember my nickname")
        with open("name.txt", "w") as file:
            name = engine.listen()
            while "sober" in name:
                name = engine.listen()
                file.write(engine.listen())
        engine.say("That is a nice name. I will never forget that")

    try:
        with open("name.txt") as f:
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
        if "time" in command:
            msg: list = [
                "Its party time.",
                "I believe its time for us to hang out?",
                "I feel like its the right time to grab coffee.",
            ]
            # choose randomly from the above list
            engine.say(random.choice(msg))
        elif "single" in command:
            engine.say("Do you want me to be?")
        elif "your name" in command:
            get_nickname()
        elif "bye" in command or "quit" in command or "fuck off" in command:
            engine.say("It was a pleasure talking to you. Hope we can hang out soon")
            break
        else:
            engine.say("Sorry, could you tell that again please? You sound like you are heavily drunk")

        engine.command = ""  # reset


if __name__ == '__main__':
    engine.greet()

    get_commands()
