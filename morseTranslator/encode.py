from .data import Morse
def encode(content) -> str:
  co: str = ''
  for letter in content.upper(): 
     co += Morse[letter]
  return co
