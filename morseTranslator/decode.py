from .data import Letter
def decode(content) -> str:
  decoded = ""
  for i in content.split(" "):
     decoded += Letter[i]
  return decoded