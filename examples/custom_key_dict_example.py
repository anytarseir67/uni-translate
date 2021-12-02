from uni_translate import translator

key = {
    '𝔞𝔟𝔠𝔡𝔢𝔣𝔤𝔥𝔦𝔧𝔨𝔩𝔪𝔫𝔬𝔭𝔮𝔯𝔰𝔱𝔲𝔳𝔴𝔵𝔶𝔷𝔄𝔅ℭ𝔇𝔈𝔉𝔊ℌℑ𝔍𝔎𝔏𝔐𝔑𝔒𝔓𝔔ℜ𝔖𝔗𝔘𝔙𝔚𝔛𝔜ℨ': 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ', 
    '𝖆𝖇𝖈𝖉𝖊𝖋𝖌𝖍𝖎𝖏𝖐𝖑𝖒𝖓𝖔𝖕𝖖𝖗𝖘𝖙𝖚𝖛𝖜𝖝𝖞𝖟𝕬𝕭𝕮𝕯𝕰𝕱𝕲𝕳𝕴𝕵𝕶𝕷𝕸𝕹𝕺𝕻𝕼𝕽𝕾𝕿𝖀𝖁𝖂𝖃𝖄𝖅': 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
} 
# define our custom key as a dict where each character in 
# the key is mapped to its respective index in the value

trans = translator(key=key) # create a translator with our custom key

print(trans.translate('𝕿𝖍𝖎𝖘 𝖎𝖘 𝖆𝖓 𝖊𝖝𝖆𝖒𝖕𝖑𝖊.'))
print(trans.translate('𝔗𝔥𝔦𝔰 𝔦𝔰 𝔞𝔫 𝔢𝔵𝔞𝔪𝔭𝔩𝔢 𝔞𝔰 𝔴𝔢𝔩𝔩.'))
print(trans.text_to_unicode('This is an example.'))
print(trans.text_to_unicode('This is an example as well.', mode=1))