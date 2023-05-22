import math

products = {
  "Product A": 20,
  "Product B": 40,
  "Product C": 50,
}

discounts = {
  "flat_10_discount": (200, 10),
  "bulk_5_discount": (10, 5),
  "bulk_10_discount": (20, 10),
  "tiered_50_discount": (30, 15),
}

fees = {
  "gift_wrap": 1,
  "shipping": 5,
}

def get_quantity(product_name):
  quantity = int(input("Enter the quantity of {}: ".format(product_name)))
  return quantity

def get_is_gift_wrapped():
  is_gift_wrapped = input("Is the product wrapped as gift? (Y/N): ") == "Y"
  return is_gift_wrapped

def calculate_subtotal(products, quantities):
  subtotal = 0
  for product_name, quantity in quantities.items():
    subtotal += products[product_name] * quantity
  return subtotal

def calculate_discount(subtotal, discounts):
  discount_name = None
  discount_amount = 0
  for discount_name, amount in discounts.items():
    if subtotal >= amount[0]:
      discount_name = discount_name
      discount_amount = amount[1]
      break
  return discount_name, discount_amount

def calculate_shipping_fee(subtotal, fees):
  shipping_fee = math.ceil(subtotal / 10) * fees["shipping"]
  return shipping_fee

def calculate_gift_wrap_fee(quantities):
  gift_wrap_fee = quantities["Product A"] * fees["gift_wrap"]
  return gift_wrap_fee

def calculate_total(subtotal, discount_name, discount_amount, shipping_fee, gift_wrap_fee):
  total = subtotal - discount_amount + shipping_fee + gift_wrap_fee
  return total

def main():
  # Get the quantity of each product
  quantities = {}
  for product_name in products:
    quantities[product_name] = get_quantity(product_name)

  # Get whether the product is wrapped as gift
  is_gift_wrapped = get_is_gift_wrapped()

  # Calculate the subtotal
  subtotal = calculate_subtotal(products, quantities)

  # Calculate the discount
  discount_name, discount_amount = calculate_discount(subtotal, discounts)

  # Calculate the shipping fee
  shipping_fee = calculate_shipping_fee(subtotal, fees)

  # Calculate the gift wrap fee
  gift_wrap_fee = calculate_gift_wrap_fee(quantities)

  # Calculate the total
  total = calculate_total(subtotal, discount_name, discount_amount, shipping_fee, gift_wrap_fee)

  # Print the details
  print("Product Name | Quantity | Total")
  for product_name, quantity in quantities.items():
    print("{:20s} | {:4d} | ${:10.2f}".format(product_name, quantity, products[product_name] * quantity))

  print("Subtotal: $%10.2f" % subtotal)
  if discount_name is not None:
    print("Discount: $%10.2f (%s)" % (discount_amount, discount_name))
  print("Shipping: $%10.2f" % shipping_fee)
  if is_gift_wrapped:
    print("Gift wrap: $%10.2f" % gift_wrap_fee)

  print("Total: $%10.2f" % total)

if __name__ == "__main__":
  main()
