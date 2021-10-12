import json
import random
import re  # regex lib
import service.temperature_service as temp
from smtplib import SMTPAuthenticationError
from text_to_speech import TextToSpeech
from service.email_sender_service import EmailSenderService
from service.wikipedia_service import WikipediaService
from service.google_service import GoogleService

engine: TextToSpeech = TextToSpeech()


def get_nickname() -> None:
    def ask_nickname() -> None:
        engine.say("You can call me anything babe i am all yours. I will remember my nickname")
        with open("files/name.txt", "w") as file:
            name = engine.listen()
            while "sober" in name:
                name = engine.listen()
                file.write(engine.listen())  # keeps deleting previous content before writing
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


def send_mail() -> None:
    email = engine.prompt("What is your email?: ")
    password = engine.prompt("What is your password? You can trust me. I will keep it a secret: ")
    email_to = engine.prompt("What is the email of that lucky person you want me to email?: ")
    subject = engine.prompt("What is the subject of the email?: ")
    msg = engine.prompt("What would  you like to tell him?: ")
    try:
        EmailSenderService(
            email,
            password,
        ).send(
            subject,
            msg,
            email_to=email_to  # receiver email
        )
    except SMTPAuthenticationError:
        engine.say("Seems like you don't completely trust me, honey. The details are wrong")
        send_mail()
    engine.say("Your email has been sent. I need a kiss in return")


def get_commands() -> None:
    while True:
        # read from terminal without input message
        command = engine.listen().lower()
        with open("files/keywords.json") as JSon:
            data: dict = json.loads(JSon.read())

        entered: bool = False
        # iterating through the parsed dictionary/map
        for keyword, messages in data.items():
            keywords = re.compile(keyword)
            if re.search(keywords, command):
                if isinstance(messages, list):
                    entered = True
                    engine.say(random.choice(messages))
                elif isinstance(messages, str):
                    entered = True
                    engine.say(messages)
        if not entered:
            if "change" in command and "voice" in command:
                engine.change_voice()
                engine.say("I changed by voice for you!")
            elif "mail" in command:
                send_mail()
            elif "your name" in command:
                get_nickname()
            elif "temperature" in command:
                engine.say(temp.get_current_temperature())
            elif "wikipedia" in command:
                engine.say("Searching in wikipedia... You can look at my face until then")
                result = WikipediaService(
                    command.strip("wikipedia").strip("search")  # remove "wikipedia", "search" before searching
                ).search()
                engine.say(result)
            elif "google" in command:
                engine.say("Googling... ")
                GoogleService(
                    command.strip("google").strip("search")
                    .strip("in").strip("for")  # remove "google", "search", "in", "for" before searching
                ).search()
            elif "bye" in command or "quit" in command or "fuck off" in command:
                engine.say("It was a pleasure talking to you. Hope we can hang out soon")
                break
            else:
                engine.say("Sorry, could you tell that again please? You sound like you are heavily drunk")


if __name__ == '__main__':
    engine.greet()

    get_commands()
