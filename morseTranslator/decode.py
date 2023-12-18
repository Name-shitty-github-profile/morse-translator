from .data import Letter
def decode(content) -> str:
  decoded = ""
  for i in content.split(" "):
     if i == " ": continue
     decoded += Letter[i]
  return decoded