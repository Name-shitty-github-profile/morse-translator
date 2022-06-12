# morse-translator
A mini morse-translator module
# encode
```py
string: str = "Some text"
import morseTranslator as mt
morse_string: str = mt.encode(string)
print(morse_string)
```
ouput
```
... --- -- . / - . -..- -
```
# decode
```py
morse_string: str = "... --- -- . / - . -..- -"
import morseTranslator as mt
string: str = mt.decode(morse_string)
print(string)
```
ouput
```
some text
```
