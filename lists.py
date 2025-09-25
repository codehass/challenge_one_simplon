products = ["Clavier", "Souris", "Ecran", "Chaise", "Bureau", "Lamp"]
prices = [45, 150, 1200, 855, 2000, 25]

products_prices = list(zip(products, prices))

filtered_products = filter(lambda item: item[1] > 30, products_prices)

filtered_products_list = list(filtered_products)

products_price_string_list = list(map(lambda item: f"{item[0]} coute {item[1]} DH", products_prices))

