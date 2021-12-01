from uni_translate import translator

key = [
    '𝔞𝔟𝔠𝔡𝔢𝔣𝔤𝔥𝔦𝔧𝔨𝔩𝔪𝔫𝔬𝔭𝔮𝔯𝔰𝔱𝔲𝔳𝔴𝔵𝔶𝔷𝔄𝔅ℭ𝔇𝔈𝔉𝔊ℌℑ𝔍𝔎𝔏𝔐𝔑𝔒𝔓𝔔ℜ𝔖𝔗𝔘𝔙𝔚𝔛𝔜ℨ',
    '𝖆𝖇𝖈𝖉𝖊𝖋𝖌𝖍𝖎𝖏𝖐𝖑𝖒𝖓𝖔𝖕𝖖𝖗𝖘𝖙𝖚𝖛𝖜𝖝𝖞𝖟𝕬𝕭𝕮𝕯𝕰𝕱𝕲𝕳𝕴𝕵𝕶𝕷𝕸𝕹𝕺𝕻𝕼𝕽𝕾𝕿𝖀𝖁𝖂𝖃𝖄𝖅'
] 
# define our custom key as a list where for each element, each character is mapped 
# to its respective index in abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ

remove = '!()'
# define our custom remove, all characters in this 
# string (can also be a list of strings) will be removed when translating

trans = translator(key=key, remove=remove) # create a translator with our custom key and remove

print(trans.translate('(!𝕿𝖍𝖎𝖘 𝖎𝖘 𝖆𝖓 𝖊𝖝𝖆𝖒𝖕𝖑𝖊.!)'))
print(trans.translate('(!𝔗𝔥𝔦𝔰 𝔦𝔰 𝔞𝔫 𝔢𝔵𝔞𝔪𝔭𝔩𝔢 𝔞𝔰 𝔴𝔢𝔩𝔩.!)'))