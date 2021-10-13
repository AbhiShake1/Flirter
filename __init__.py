if __name__ == '__main__':
    from core.text_to_speech import TextToSpeech
    from main import init

    while True:
        trigger = TextToSpeech.listen_in_background().lower()
        if ("babe" in trigger) or ("baby" in trigger):
            break

    init(TextToSpeech())
