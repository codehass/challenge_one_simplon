from functions import *

from lists import *


products_prices = get_products_prices(products, prices)

# products_prices.sort(key=priceSortFunction)

# display_list(products_prices, "Ascendent order product by price: ")

# max_element = products_prices[-1]
# min_element = products_prices[0]

# print("********")
# print("Expensive product: ", max_element)
# print("Cheap product: ", min_element)
# print("********")


choices = ["1- Add a new product", "2- Search by name","3- Display list", "4- Filter products price > 30", "5- List of product using f-string", "6- List product with LUXE", "7- Exit"]

def menu():
  while True:
    print("--------Menu-------")
    print("-------------------")
    
    for choice in choices:
      print(" ", choice)

    print("\n")
    
    try:
      choice = int(input("Enter a value: "))
    except ValueError:
      print("Invalid input. Please enter a number.")
      continue

    if choice == 1:
      product_name = input("Enter product name: ").strip()
      try:
        product_price = float(input("Enter product price: ").strip())
      except ValueError:
        print("Invalid price. Please enter a number.")
        continue

      if product_name:
        addNewProduct(product_name, product_price, products, prices)
        print(f"'{product_name}' added successfully!\n")
      else:
        print("Please enter a valid product name.")

    elif choice == 2:
      product_name = input("Enter search product name: ").strip()
      current_products_prices = get_products_prices(products, prices)
      products_list_searched = search_product_by_name(product_name, current_products_prices)
      if products_list_searched:
        display_list(products_list_searched, "Searched product:")
      else:
        print("No product found with the entered name.")

    elif choice == 3:
      current_products_prices = get_products_prices(products, prices)
      display_list(current_products_prices, "List of all existing products:")

    elif choice == 4:
      current_products_prices = get_products_prices(products, prices)
      display_list(filtered_products(current_products_prices), "Products with price > 30 DH:")

    elif choice == 5:
      current_products_prices = get_products_prices(products, prices)
      display_list(products_price_string_list(current_products_prices), "Products as strings:")

    elif choice == 6:
      current_products_prices = get_products_prices(products, prices)
      display_list(luxury_products(current_products_prices), "Luxury products:")

    elif choice == 7:
      print("Exiting program. Goodbye!")
      break

    else:
      print("Invalid choice. Please try again.")


menu()