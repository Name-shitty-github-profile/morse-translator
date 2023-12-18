from .data import Letter
def decode(content) -> str:
  for encoded_char in Letter.keys():
     content.replace(encoded_char, Letter[encoded_char])
  return content
