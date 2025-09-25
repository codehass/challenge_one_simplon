from functions import display_list, priceSortFunction
from lists import products_prices, filtered_products_list, products_price_string_list


display_list(products_prices, "List of existing products: ")

display_list(filtered_products_list,'filtered_products')

display_list(products_price_string_list,'List of products as string using f-string')

products_prices.sort(key=priceSortFunction)

display_list(products_prices, "Ascendent by product price: ")

max_element = max(products_prices)

print(max_element)
