# uni-translate
Python library to "translate" a variety of unicode special characters to normal text

can be used as a command line util for strings and text files, or as a library for easier and more flexible integration

# Documentation:
* ##  [class] translator
* * ### [kwarg] Union[dict, List[str]]=None key:
* * * ### key used to contruct a translation table, can be a list of strings contaning 52 characters (one for each letter, upper and lowercase), or a dict contaning key/value pairs that map each character in the key to a character in the value. (default is provided)

<br/>

* * ### [kwarg] Union[str, List[str]]=None remove:
* * * ### characters to be stripped during translation (default is provided)

<br/>

* * ### [kwarg] (bool)=False debug:
* * * ### toggles debug prints in the \_\_init__

<br/>

* * ### [method] translate -> str:
* * * ### [arg] (str) text: text to be translated

<br/>

* * ### [staticmethod] _trans -> str:
* * * ### method to translate text via the given table
* * * ### [arg] (str) text: text to be translated
* * * ### [arg] Union[dict, Union[List[str], Tuple[str]]] table: table to use for translation, when a list or tuple is passed, the first element is treated as the key and the second element is treated as the value. dict should only be passed if it is a valid translation table (as obtained from str.maketrans)

<br/>

* * ### [staticmethod] clean_key -> Tuple[str]:
* * * ### returns the key cleaned of "normal" characters and duplicates, and its respective alphabet value
* * * ### [arg] (str) key - key to be cleaned