import speech_recognition as sr


class SpeechRecognizer(sr.Recognizer, sr.):
    def __enter__(self):
        pass

    def __exit__(self, exc_type, exc_value, traceback):
        pass
