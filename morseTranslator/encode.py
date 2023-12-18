from .data import Morse
def encode(content) -> str:
  for i in [" ", ".", "/", "-"]:
     content = replace(i, "")
  for letter in Morse.keys():
     content = content.replace(letter, f"{Morse[letter]} ")
  return content[:-1]
