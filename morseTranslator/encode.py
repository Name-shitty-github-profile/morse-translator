from .data import Morse
def encode(content) -> str:
  content = content.replace(" ", "").replace(".", "").replace("_", ".")
  for letter in Morse.keys():
     content = content.replace(letter, f"{Morse[letter]} ")
  return content[:-1]
