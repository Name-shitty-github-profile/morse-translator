from .data import Morse
def encode(content) -> str:
  co: str = ''
  for letter in content.upper(): co += f'{Morse[letter]} '
  return co
