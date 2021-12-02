from uni_translate import translator

trans = translator() # run with default config
x = "Ⓣⓗⓘⓢ ⓘⓢ ⓐⓝ ⓔⓧⓐⓜⓟⓛⓔ." # example unicode string to translate
print(trans.translate(x)) # print the translated string
print(trans.text_to_unicode('This is an example.', mode=10))