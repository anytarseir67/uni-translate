from uni_translate import translator
import os, sys

def main() -> None:
    text = None
    if '-t' in sys.argv:
        text = ' '.join(sys.argv[sys.argv.index('-t')+1:])
        if text.strip() == '':
            text = None
    if text == None:
        text = input('text to translate? ')
    if os.path.exists(os.path.dirname(text)):
        with open(text, 'rt', encoding='utf-8') as f:
            text = f.read()
    translated = translator().translate(text)
    print(translated)

if __name__ == "__main__":
    main()