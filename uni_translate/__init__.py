from typing import Union, List, Tuple

_default_key = ['๐๐๐ ๐ก๐ข๐ฃ๐ค๐ฅ๐ฆ๐ง๐จ๐ฉ๐ช๐ซ๐ฌ๐ญ๐ฎ๐ฏ๐ฐ๐ฑ๐ฒ๐ณ๐ด๐ต๐ถ๐ท๐๐โญ๐๐๐๐โโ๐๐๐๐๐๐๐๐โ๐๐๐๐๐๐๐โจ',
'๐๐๐๐๐๐๐๐๐๐๐๐๐๐๐๐๐๐๐๐๐๐๐๐๐๐๐ฌ๐ญ๐ฎ๐ฏ๐ฐ๐ฑ๐ฒ๐ณ๐ด๐ต๐ถ๐ท๐ธ๐น๐บ๐ป๐ผ๐ฝ๐พ๐ฟ๐๐๐๐๐๐',
'๐ช๐ซ๐ฌ๐ญ๐ฎ๐ฏ๐ฐ๐ฑ๐ฒ๐ณ๐ด๐ต๐ถ๐ท๐ธ๐น๐บ๐ป๐ผ๐ฝ๐พ๐ฟ๐๐๐๐๐๐๐๐๐๐๐๐๐๐๐๐๐๐๐๐๐ ๐ก๐ข๐ฃ๐ค๐ฅ๐ฆ๐ง๐จ๐ฉ',
'๐ถ๐ท๐ธ๐น๐๐ป๐๐ฝ๐พ๐ฟ๐๐๐๐๐๐๐๐๐๐๐๐๐๐๐๐๐๐ต๐๐๐ธ๐น๐ข๐ป๐ผ๐ฅ๐ฆ๐ฟ๐๐ฉ๐ช๐ซ๐ฌ๐๐ฎ๐ฏ๐ฐ๐ฑ๐ฒ๐ณ๐ด๐ต',
'๐๐๐๐๐๐๐๐๐๐๐๐๐๐๐ ๐ก๐ข๐ฃ๐ค๐ฅ๐ฆ๐ง๐จ๐ฉ๐ช๐ซ๐ธ๐นโ๐ป๐ผ๐ฝ๐พโ๐๐๐๐๐โ๐โโโ๐๐๐๐๐๐๐โค',
'๏ฝ๏ฝ๏ฝ๏ฝ๏ฝ๏ฝ๏ฝ๏ฝ๏ฝ๏ฝ๏ฝ๏ฝ๏ฝ๏ฝ๏ฝ๏ฝ๏ฝ๏ฝ๏ฝ๏ฝ๏ฝ๏ฝ๏ฝ๏ฝ๏ฝ๏ฝ๏ผก๏ผข๏ผฃ๏ผค๏ผฅ๏ผฆ๏ผง๏ผจ๏ผฉ๏ผช๏ผซ๏ผฌ๏ผญ๏ผฎ๏ผฏ๏ผฐ๏ผฑ๏ผฒ๏ผณ๏ผด๏ผต๏ผถ๏ผท๏ผธ๏ผน๏ผบ',
'แดสแดแดแด๊ฐษขสษชแดแดสแดษดแดแดQส๊ฑแดแดแด แดกxสแดขแดสแดแดแด๊ฐษขสษชแดแดสแดษดแดแดQส๊ฑแดแดแด แดกxสแดข',
'๐ฐ๐ฑ๐ฒ๐ณ๐ด๐ต๐ถ๐ท๐ธ๐น๐บ๐ป๐ผ๐ฝ๐พ๐ฟ๐๐๐๐๐๐๐๐๐๐๐ฐ๐ฑ๐ฒ๐ณ๐ด๐ต๐ถ๐ท๐ธ๐น๐บ๐ป๐ผ๐ฝ๐พ๐ฟ๐๐๐๐๐๐๐๐๐๐',
'โแตฆ๐ธ๐นโ๐ป๐ฐโแตขโฑผโโโโโโแตฉแตฃโโแตคแตฅ๐โแตง๐โแตฆ๐ธ๐นโ๐ป๐ฐโแตขโฑผโโโโโโแตฉแตฃโโแตคแตฅ๐โแตง๐',
'แตแตแถแตแตแถ แตสฐโฑสฒแตหกแตโฟแตแตแต สณหขแตแตแตสทหฃสธแถปแดฌแดฎแถแดฐแดฑแถ แดณแดดแดตแดถแดทแดธแดนแดบแดผแดพแต แดฟหขแตแตโฑฝแตหฃสธแถป',
'โโโโโโโโโโโโโโโโโ โกโขโฃโคโฅโฆโงโจโฉโถโทโธโนโบโปโผโฝโพโฟโโโโโโโโโโโโโโโโ',
'เธเนฯเนัลฆ๏ปฎัเนืะบษญเนเธ เนืงแปฃะณเธฃีเธขืฉเธฌืืฅีนเธเนฯเนัลฆ๏ปฎัเนืะบษญเนเธ เนืงแปฃะณเธฃีเธขืฉเธฌืืฅีน',
'ฮฑแฆฦิาฝฯษ ิฮนสฦสษฑษณฯฯฯษพสฦฯสษฏxแงศฅฮฑแฆฦิาฝฯษ ิฮนสฦสษฑษณฯฯฯษพสฦฯสษฏxแงศฅ',
'วษฎฦษษสษขษฆษจสำสสีผึึีฆสึศถสสีกำผสสวษฎฦษษสษขษฆษจสำสสีผึึีฆสึศถสสีกำผสส',
'ฤแชฦษษสษ ษงฤฑสฦฦษฑลฦกโีฆเฝสษฌลณ?ทแฟณาณแงสฤแชฦษษสษ ษงฤฑสฦฦษฑลฦกโีฆเฝสษฌลณ?ทแฟณาณแงส',
'เธเนยขเปฤfเบhiเธงklเนเบเปpเนrลtเธเธเบxเธฏเบเธเนยขเปฤfเบhiเธงklเนเบเปpเนrลtเธเธเบxเธฏเบ',
'๐๐๐๐๐๐๐ ๐ก๐ข๐ฃ๐ค๐ฅ๐ฆ๐ง๐จ๐ฉ๐ช๐ซ๐ฌ๐ญ๐ฎ๐ฏ๐ฐ๐ฑ๐ฒ๐ณ๐๐๐๐๐๐๐๐๐๐๐๐๐๐๐๐๐๐๐๐๐๐๐๐๐๐',
'๐ข๐ฃ๐ค๐ฅ๐ฆ๐ง๐จ๐ฉ๐ช๐ซ๐ฌ๐ญ๐ฎ๐ฏ๐ฐ๐ฑ๐ฒ๐ณ๐ด๐ต๐ถ๐ท๐ธ๐น๐บ๐ป๐๐๐๐๐๐๐๐๐๐๐๐๐๐๐๐๐๐๐๐๐๐๐๐๐ ๐ก',
'๐๐๐๐๐๐๐๐๐๐๐ ๐ก๐ข๐ฃ๐ค๐ฅ๐ฆ๐ง๐จ๐ฉ๐ช๐ซ๐ฌ๐ญ๐ฎ๐ฏ๐ผ๐ฝ๐พ๐ฟ๐๐๐๐๐๐๐๐๐๐๐๐๐๐๐๐๐๐๐๐๐๐',
'๐๐๐๐๐๐๐๐๐๐๐๐๐๐๐๐๐๐๐๐๐๐๐ ๐ก๐ข๐ฃ๐ฐ๐ฑ๐ฒ๐ณ๐ด๐ต๐ถ๐ท๐ธ๐น๐บ๐ป๐ผ๐ฝ๐พ๐ฟ๐๐๐๐๐๐๐๐๐๐',
'ฮBแDฮฃFGฮIJKแMะำจPQะฏฦงฦฌะฆVะฉXYZฮBแDฮฃFGฮIJKแMะำจPQะฏฦงฦฌะฆVะฉXYZ',
'ฮฑะฒยขโัฦgะฝฮนื ะบโะผฮทฯฯqัััฯฮฝฯฯัzฮฑะฒยขโัฦgะฝฮนื ะบโะผฮทฯฯqัััฯฮฝฯฯัz',
'รฅรยขรรชยฃghรฏjklmรฑรฐรพqrยงโ ยตvwxยฅzรรรรรยฃGHรJKLMรฑรรพQRยงโ รVWรยฅZ',
'โณเธฟโตฤษโฃโฒโฑงลJโญโฑ โฅโฆรโฑQโฑคโดโฎษVโฉำพษโฑซโณเธฟโตฤษโฃโฒโฑงลJโญโฑ โฅโฆรโฑQโฑคโดโฎษVโฉำพษโฑซ',
'ๅไนๅแชไนๅแถๅไธจ๏พาใฅ็ชๅ ใๅฉษๅฐบไธใใฉแฏๅฑฑไนใไนๅไนๅแชไนๅแถๅไธจ๏พาใฅ็ชๅ ใๅฉษๅฐบไธใใฉแฏๅฑฑไนใไน',
'๏พไนแใไน๏ฝทใ ใ๏พ๏พใบ๏พ๏พถๅใฎ๏ฝฑใๅฐบไธ๏ฝฒใฒโW๏พ๏พไน๏พไนแใไน๏ฝทใ ใ๏พ๏พใบ๏พ๏พถๅใฎ๏ฝฑใๅฐบไธ๏ฝฒใฒโW๏พ๏พไน',
'ฤารงีชาฝฦึีฐรฌสาำสีฒึึีฆษพสีงีดัตีกรีพีศบฮฒโปแ ฦฦฦวถฤฏูา ๊โฑฎแ เถงฯาจเฝ ฯอฒิฑแปผเฐแฏำษ',
'แฉแทแแชEแดGแผIแKแชแฐแOแญแซแแTแแฏแฏแญYแแฉแทแแชEแดGแผIแKแชแฐแOแญแซแแTแแฏแฏแญYแ',
'๐ฐ๐ฑ๐ฒ๐ณ๐ด๐ต๐ถ๐ท๐ธ๐น๐บ๐ป๐ผ๐ฝ๐พ๐ฟ๐๐๐๐๐๐๐๐๐๐๐ฐ๐ฑ๐ฒ๐ณ๐ด๐ต๐ถ๐ท๐ธ๐น๐บ๐ป๐ผ๐ฝ๐พ๐ฟ๐๐๐๐๐๐๐๐๐๐',
'๐๐๐๐๐๐๐๐๐๐๐๐๐๐๐๐๐ ๐ก๐ข๐ฃ๐ค๐ฅ๐ฆ๐ง๐จ๐ฉ๐๐๐๐๐๐๐๐๐๐๐๐๐๐๐๐๐ ๐ก๐ข๐ฃ๐ค๐ฅ๐ฆ๐ง๐จ๐ฉ',
'โโโโโ โกโขโฃโคโฅโฆโงโจโฉโชโซโฌโญโฎโฏโฐโฑโฒโณโดโตโโโโโ โกโขโฃโคโฅโฆโงโจโฉโชโซโฌโญโฎโฏโฐโฑโฒโณโดโต',
'ะฐััโัfะะััะบlะผะธะพัqััััvััะzะฐััโัfะะััะบlะผะธะพัqััััvััะz',
'แแแญแแฟแปแแแแแแจแ แญแแจแแชแแแแแ แธแแแแแญแแฟแปแแแแแแจแ แญแแจแแชแแแแแ แธแแ',
'๐๐๐๐๐๐แต๐๐แ๐๐๐๐๊๐๐๐๐๐๐ตแแ๐๐โฑฟ๐๐๐๐๐๐แต๐๐แ๐๐๐๐๊๐๐๐๐๐๐ตแแ๐๐โฑฟ',
'โ โ โ โ โ โ โ โ โ โ โ โ โ โ โ โ โ โ โ โ โ ฅโ งโ บโ ญโ ฝโ ตโ โ โ โ โ โ โ โ โ โ โ โ โ โ โ โ โ โ โ โ โ ฅโ งโ บโ ญโ ฝโ ต',
'๐ฎ๐ฏ๐ฐ๐ฑ๐ฒ๐ณ๐ด๐ต๐ถ๐ท๐ธ๐น๐บ๐ป๐ผ๐ฝ๐พ๐ฟ๐๐๐๐๐๐๐๐๐ฎ๐ฏ๐ฐ๐ฑ๐ฒ๐ณ๐ด๐ต๐ถ๐ท๐ธ๐น๐บ๐ป๐ผ๐ฝ๐พ๐ฟ๐๐๐๐๐๐๐๐',
'๐บ๐ป๐ผ๐ฝ๐พ๐ฟ๐๐๐๐๐๐๐๐๐๐๐๐๐๐๐๐๐๐๐๐๐บ๐ป๐ผ๐ฝ๐พ๐ฟ๐๐๐๐๐๐๐๐๐๐๐๐๐๐๐๐๐๐๐๐',
'๐๐๐๐๐๐๐๐๐๐๐๐๐๐๐๐๐๐๐๐๐๐๐๐๐๐๐๐๐๐๐๐๐๐๐๐๐๐๐๐๐๐๐๐๐๐๐๐๐๐๐๐']

_default_remove = 'ใใใใโโ[ฬฬฒ]โฆโงโฆโฆ๏ดพ๏ดฟโฆโฆ.,<>/?;:"\'{}[]|\\=+-_()*&^%$#@!`~โฆ\อ\ฬบ\ฬฝ\อ\ฬพ\อ\อ\า\ฬ\ฬค\ฬ\ฬท\ฬ\ฬ\ฬ\ฬถ\ฬฒ\ฬณ\ฬ\ฬฟ' #this looks fucking cursed in vscode

class translator:
    __slots__ = ('alph', 'chars', 'table', 'rtables')
    
    def __init__(self, *, key: Union[dict, List[str]]=_default_key, remove: Union[bool, str]=_default_remove, debug: bool=False) -> None:
        if not remove: 
            remove = ""
        else:
            remove = _default_remove

        if isinstance(key, list):
            temp_key = {}
            self.rtables = []
            for x in key:
                cleaned = self.clean_key(x)
                temp_key[cleaned[0]] = cleaned[1]

            for _key in key:
                self.rtables.append(str.maketrans('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ', _key))
            key = temp_key

        else:
            self.rtables = []
            for _key in key:
                self.rtables.append(str.maketrans(key[_key], _key))

        if isinstance(remove, list):
            temp_remove = ''.join(remove)
            remove = temp_remove

        if debug:
            print('\n'.join([f'{x}, {key[x]}' for x in key]))
            print('\n'.join(remove))

        self.alph = ""
        self.chars = ""
        for x in key.keys():
            self.chars += x
            self.alph += key[x]
        self.table = str.maketrans(self.chars, self.alph, remove)

    def translate(self, text: str) -> str:
        "unicode text to 'normal' text"
        return translator._trans(text, self.table)

    def text_to_unicode(self, text: str, *, mode: int=0) -> str:
        "'normal' text to unicode text"
        return translator._trans(text, self.rtables[mode])

    @staticmethod
    def _trans(text: str, table: Union[dict, Union[List[str], Tuple[str, str]]]) -> str:
            if isinstance(table, (list, tuple)):
                table = str.maketrans(table[0], table[1])
            return text.translate(table)

    @staticmethod
    def clean_key(key: str) -> Tuple[str, str]:
        alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
        cleaned_chars = ""
        cleaned_alph = ""
        for i, char in enumerate(key):
            if char not in alphabet:
                if char not in cleaned_chars:
                    cleaned_chars += char
                    cleaned_alph += alphabet[i]
        return cleaned_chars, cleaned_alph
