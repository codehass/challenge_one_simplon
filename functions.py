def display_list(list, text):
  print(text)

  for item in list:
    print(item)

def priceSortFunction(e):
  return e[1]

def luxuryFunction(item):
  if item[1] > 1000:
    return f"{item[0]} coute {item[1]} DH (LUXE)"
  else:
    return f"{item[0]} coute {item[1]} DH"