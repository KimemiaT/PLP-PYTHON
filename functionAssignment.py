price = int(input("Enter price:"))
discount_percent = int(input("Enter discount percentage:"))
discount_percent /= 100

def calculate_discount(price, discount_percent):
    if discount_percent < (20 / 100):
        print("Original Price:", price)
    elif discount_percent >= (20 / 100):
        discount = price * discount_percent
        discounted_price = price - discount
        print("Discounted Price:", discounted_price)

# Call the function
calculate_discount(price, discount_percent)
