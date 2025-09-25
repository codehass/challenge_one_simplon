from helpers import luxuryFunction

def display_list(list, text):
  print("-------------------")
  print(text)
  print("-------------------")

  for item in list:
    print(" ",item)
  print("\n")

def get_products_prices(products, prices):
    return list(zip(products, prices))

def addNewProduct(product_name, product_price,products_list, prices_list):
  products_list.append(product_name)
  prices_list.append(product_price)

def search_product_by_name(product_name, products_list):
  return list(filter(lambda product: product[0] == product_name, products_list))

def filtered_products(list_product: list)-> list:
  return list(filter(lambda item: item[1] > 30, list_product))

def products_price_string_list (list_product: list)-> list:
  return list(map(lambda item: f"{item[0]} coute {item[1]} DH", list_product))

def luxury_products(list_product: list)-> list:
  return list(map(luxuryFunction, list_product))