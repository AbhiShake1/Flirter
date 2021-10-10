import ctypes
import locale
import pyttsx3  # text to speech lib
import speech_recognition
import speech_recognition as sr
import datetime as dt
from threading import Thread


class TextToSpeech(pyttsx3.Engine):  # inheriting from pyttsx3 module

    def __init__(self):
        pyttsx3.init()
        super().__init__()
        self.hour: int = int(dt.datetime.now().hour)
        # 2nd voice. usually female voice
        self.voice_index = 1
        self.__set_voice__()

    def __set_voice__(self) -> None:
        voice: str = self.getProperty("voices")[self.voice_index].id
        self.setProperty("voice", voice)

    # overriding from superclass to print whats typed
    def say(self, msg: str, **kwargs) -> None:
        super().say(msg)
        print(msg)
        self.runAndWait()
        self.command = ""  # reset after speaking

    # noinspection PyAttributeOutsideInit
    def get_input(self) -> None:
        self.command = input("Type here if you are too shy to speak: ")

    # noinspection PyAttributeOutsideInit
    def listen(self, timeout=3) -> str:
        input_thread = Thread(target=self.get_input)
        input_thread.daemon = True  # Terminate thread when the main program terminates
        input_thread.start()
        input_thread.join(timeout=timeout)  # Stop listening to terminal input after 3 seconds

        if not self.command:
            r = sr.Recognizer()
            with sr.Microphone() as cmd:
                print("Listening..")
                # adjust for background noise which breaks listening
                r.adjust_for_ambient_noise(cmd)
                # do not translate message if user takes gap < 1 second while speaking
                # r.pause_threshold = 1
                audio = r.listen(cmd)
            try:
                # get and set default language of system
                self.command = r.recognize_google(
                    audio, language=locale.windows_locale
                    [ctypes.windll.kernel32.GetUserDefaultUILanguage()]
                )
                print(self.command)
            except speech_recognition.UnknownValueError:
                return "Could not understand. Are you sober?"

        return self.command

    def change_voice(self):
        voices = self.getProperty("voices")
        # switch between voices
        self.voice_index = (self.voice_index + 1) % len(voices)
        self.__set_voice__()

    def greet(self) -> None:
        greeting: str = "Hey babe, wanna have some fun before you sleep?"
        if 6 <= self.hour < 12:
            greeting = "Good Morning babe, how are you doin?"
        elif 12 <= self.hour < 18:
            greeting = "Good Afternoon babe, how are you doin?"
        elif 18 <= self.hour < 23:
            greeting = "Good Evening babe, how was your day?"

        self.say(greeting)
