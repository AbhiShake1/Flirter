import pyttsx3  # text to speech lib
import datetime as dt
import speech_recognition as sr
from threading import Thread


class TextToSpeech(pyttsx3.Engine):  # inheriting from pyttsx3 module

    def __init__(self):
        pyttsx3.init()
        super().__init__()
        self.hour: int = int(dt.datetime.now().hour)
        # last voice index. usually female voice
        default_voice: list = self.getProperty("voices")[-1].id
        self.setProperty("voice", default_voice)

    # overriding from superclass to print whats typed
    def say(self, msg: str, **kwargs):
        super().say(msg)
        print(msg)
        self.runAndWait()
        self.command = ""  # reset after speaking

    # noinspection PyAttributeOutsideInit
    def get_input(self):
        self.command = input("Type here if you are too shy to speak: ")

    # noinspection PyAttributeOutsideInit
    def listen(self) -> str:
        input_thread = Thread(target=self.get_input)
        input_thread.daemon = True  # Terminate thread when the main program terminates
        input_thread.start()
        input_thread.join(timeout=3)  # Stop listening to terminal input after 3 seconds

        if not self.command:
            r = sr.Recognizer()
            with sr.Microphone() as cmd:
                print("Listening..")
                # adjust for background noise which breaks listening
                r.adjust_for_ambient_noise(cmd)
                audio = r.listen(cmd)
            try:
                self.command = r.recognize_google(audio, language="en-IN")  # indian english
                print(self.command)
            except Exception:
                return "Could not understand. Are you sober?"

        return self.command

    def greet(self) -> None:
        greeting: str = "Hey babe, wanna have some fun before you sleep?"
        if 6 <= self.hour < 12:
            greeting = "Good Morning babe, how are you doin?"
        elif 12 <= self.hour < 18:
            greeting = "Good Afternoon babe, how are you doin?"
        elif 18 <= self.hour < 23:
            greeting = "Good Evening babe, how was your day?"

        self.say(greeting)
