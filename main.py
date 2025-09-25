from functions import display_list, priceSortFunction
from lists import products_prices, filtered_products_list, products_price_string_list, luxury_products


display_list(products_prices, "List of existing products: ")

display_list(filtered_products_list,"filtered_products: ")

display_list(products_price_string_list,"List of products as string using f-string: ")

products_prices.sort(key=priceSortFunction)

display_list(products_prices, "Ascendent by product price: ")

max_element = products_prices[-1]
min_element = products_prices[0]

print("********")
print("Expensive product: ", max_element)
print("Cheap product: ", min_element)
print("********")

display_list(luxury_products, "Luxury products: ")
