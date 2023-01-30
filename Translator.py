from googletrans import Translator



def Translation():
    translator = Translator()
    untranslated = open('untranslated.txt', 'r')
    translated = open('translated.txt', 'w')


    for line in untranslated:
        translated_text = translator.translate(line)
        x = translated_text.text
        translated.write(x)
        translated.write('\n')


    untranslated.close()
    translated.close()

