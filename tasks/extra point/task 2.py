# Simulate a basic shopping cart system


#Display a menu with at least 5 items and prices

#Allow user to select items and quantities

#Calculate subtotal, tax (7%), and total

#Apply 10% discount if subtotal > $50

#Display a detailed receipt




def shopping_cart():
    print("=== Welcome to malishop ===")
    
    # Store inventory with item codes
    inventory = {
        1: {"name": "Bread", "price": 2.50},
        2: {"name": "Milk", "price": 3.00},
        3: {"name": "Eggs", "price": 4.00},
        4: {"name": "Apples", "price": 1.75},
        5: {"name": "Chocolate", "price": 2.25}
    }
    
    cart = {}
    
    # Display menu
    print("\n=== Available Items ===")
    print("Code | Item        | Price")
    print("-" * 25)
    for code, item in inventory.items():
        print(f"{code:4} | {item['name']:11} | ${item['price']:.2f}")
    
    print("\nEnter item code (0 to finish)")
    print("=" * 30)
    
    # Shopping loop
    while True:
        try:
            item_code = int(input("\nEnter item code: "))
            
            if item_code == 0:
                break
            elif item_code not in inventory:
                print("Invalid item code! Please choose from the list.")
                continue
            
            quantity = int(input(f"Enter quantity for {inventory[item_code]['name']}: "))
            
            if quantity <= 0:
                print("Quantity must be positive!")
                continue
            
            # Add to cart
            if item_code in cart:
                cart[item_code]["quantity"] += quantity
            else:
                cart[item_code] = {
                    "name": inventory[item_code]["name"],
                    "price": inventory[item_code]["price"],
                    "quantity": quantity
                }
            
            print(f"Added {quantity} x {inventory[item_code]['name']} to cart.")
            
        except ValueError:
            print("Please enter valid numbers!")
    
    # Check if cart is empty
    if not cart:
        print("\nYour cart is empty. Goodbye!")
        return
    
    # Calculate receipt
    print("\n" + "=" * 40)
    print("RECEIPT".center(40))
    print("=" * 40)
    
    subtotal = 0
    tax_rate = 0.07  # 7% tax
    
    # Display items
    print("\nItems Purchased:")
    print("-" * 40)
    for item in cart.values():
        item_total = item["price"] * item["quantity"]
        subtotal += item_total
        print(f"{item['name']:15} x{item['quantity']:3} @ ${item['price']:5.2f} = ${item_total:6.2f}")
    
    # Calculate totals
    tax = subtotal * tax_rate
    
    # Apply discount if subtotal > 50
    discount = 0
    if subtotal > 50:
        discount = subtotal * 0.10
    
    total = subtotal + tax - discount
    
    # Display totals
    print("\n" + "-" * 40)
    print(f"{'Subtotal:':30} ${subtotal:7.2f}")
    
    if discount > 0:
        print(f"{'Discount (10%):':30} -${discount:7.2f}")
    
    print(f"{'Tax (7%):':30} ${tax:7.2f}")
    print("=" * 40)
    print(f"{'TOTAL:':30} ${total:7.2f}")
    print("=" * 40)
    print("\nThank you for shopping with us! 🛒")

# Run the shopping cart
shopping_cart()
