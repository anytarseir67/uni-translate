from uni_translate import translator

trans = translator() # run with default config
x = "Ⓣⓗⓘⓢ ⓘⓢ ⓐⓝ ⓔⓧⓐⓜⓟⓛⓔ." # example unicode string to translate
print(trans.translate(x)) # print the translated string