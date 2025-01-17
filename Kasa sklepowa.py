import datetime

print("Wybierz opcję \n1. => Lista wszystkich produktów \n2. => Zakupy \n3. => Zakończ program")

x = (input("Wybierz 1, 2 lub 3: "))

products = {
    "001": ("Masło Extra", 6.50),
    "002": ("Chleb wiejski", 4.50),
    "003": ("Makaron Babuni", 9.20),
    "004": ("Dżem truskawkowy", 8.10),
    "005": ("Kiełbasa myśliwska", 29.00),
    "006": ("Szynka konserwowa", 22.00),
    "007": ("Chipsy paprykowe", 6.00),
    "008": ("Serek wiejski", 3.50),
    "009": ("Sól kuchenna", 2.70),
    "010": ("Cukier kryształ", 3.20),
}


if x == "1":

    print("KOD KRESKOWY | NAZWA")
    for code, (name, price) in products.items():
        print(f"{code} | {name}")

    print("Wybierz opcję \n1. => Lista wszystkich produktów \n2. => Zakupy \n3. => Zakończ program")


if x == "3":
    exit()

if x == "2":
    print()

purchased_products = {}

total_price = 0

VAT_RATE = 1.23
VAT_RATE1 = 0.23

done = False

while not done:
  product_code = input("Kod kreskowy lub wydruk paragonu(P): ")

  if product_code.upper() == "P":
    done = True
    continue

  if product_code in products:
      product_name, product_price = products[product_code]

      print(f"{product_name}")

      price = product_price * VAT_RATE
      rounded_price = round(price, 2)
      purchased_products[product_code] = (product_name, rounded_price)
      total_price += rounded_price
      total_price = round(total_price, 2)

      print(f"Cena łączna: {total_price:.2f} zł")

  else:
    print("Zły kod produktu. Spróbuj ponownie.")


total_price_without_vat = total_price / (1 + VAT_RATE1)
vat = round(total_price - total_price_without_vat, 2)

now = datetime.datetime.now()
purchase_date = now.strftime("%m/%d/%Y %H:%M:%S")

print("---------------------------------")
print("Paragon:")
print(f"Data zakupu: {purchase_date}")
print("---------------------------------")

for product_code, (product_name, product_price) in purchased_products.items():
  print(f"{product_name}: {product_price:.2f} zł")

print("---------------------------------")
print(f"Do zapłaty: {total_price}" " zł")
print(f"W tym vat: {vat}" " zł")
print("---------------------------------")