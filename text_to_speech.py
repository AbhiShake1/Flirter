import ctypes
import locale

import pyautogui
import pyttsx3  # text to speech lib
import speech_recognition
import speech_recognition as sr
import datetime as dt


class TextToSpeech(pyttsx3.Engine):  # inheriting from pyttsx3 module

    def __init__(self):
        pyttsx3.init()
        super().__init__()
        self.__hour__: int = int(dt.datetime.now().hour)
        self.__command__: str = ""
        # 2nd voice. usually female voice
        self.__voice_index__: int = 1
        self.__set_voice__()

    def __set_voice__(self) -> None:
        voice: str = self.getProperty("voices")[self.__voice_index__].id
        self.setProperty("voice", voice)

    def prompt(self, msg: str) -> str:
        self.say(msg)
        return self.listen()

    # overriding from superclass to print whats typed
    def say(self, msg: str, **kwargs) -> None:
        super().say(msg)
        print(msg)
        self.runAndWait()
        self.__command__ = ""  # reset after speaking

    # noinspection PyAttributeOutsideInit
    def listen(self) -> str:
        self.__command__ = pyautogui.prompt("Type here if you are too shy to talk to me\n"
                                            "Press CANCEL if you are not ")

        if not self.__command__:
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
                self.__command__ = r.recognize_google(
                    audio, language=locale.windows_locale
                    [ctypes.windll.kernel32.GetUserDefaultUILanguage()]
                )
                print(self.__command__)
            except speech_recognition.UnknownValueError:
                return "Could not understand. Are you sober?"

        return self.__command__

    def change_voice(self) -> None:
        # since the interpreter thinks its an object thanks to annotation in pyttsx3 engine
        # but it is actually a list, we sliced it without changing its content [::] 0-end
        voices: list = self.getProperty("voices")[::]
        # switch between voices
        self.__voice_index__ = (self.__voice_index__ + 1) % len(voices)
        self.__set_voice__()

    def greet(self) -> None:
        greeting: str = "Hey babe, wanna have some fun before you sleep?"
        if 6 <= self.__hour__ < 12:
            greeting = "Good Morning babe, how are you doin?"
        elif 12 <= self.__hour__ < 18:
            greeting = "Good Afternoon babe, how are you doin?"
        elif 18 <= self.__hour__ < 23:
            greeting = "Good Evening babe, how was your day?"

        self.say(greeting)
