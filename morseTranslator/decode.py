from .data import Letter
def decode(content) -> str:
  deco: str = ''
  for thing in content.split(' '): 
    if thing != '': deco += f'{Letter[thing]}'
  return deco.lower()
