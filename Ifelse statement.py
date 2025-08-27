def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        discount_amount = price * (discount_percent / 100)
        final_price = price - discount_amount
        return final_price
    else:
        return  price
    
    # Ask user for input
price = float(input("Enter the original price: "))
discount_percent = float(input("Enter the discount percentage: "))

# Call the function
final_price = calculate_discount(price, discount_percent)

# Show the result
if discount_percent >= 20:
    print(f"The final price after {discount_percent}% discount is: {final_price}")
else:
    print(f"No discount applied. The price remains: {final_price}")