from uni_translate import translator
import os

def main() -> None:
    text = input('text to translate?')
    if os.path.exists(os.path.dirname(text)):
        with open(text, 'rt', encoding='utf-8') as f:
            text = f.read()
    translated = translator().translate(text)
    print(translated)

if __name__ == "__main__":
    main()