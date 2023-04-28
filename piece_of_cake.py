def get_recipe_price(prices, optionals=[], **products):
    # Initialize the total price to 0
    total_price = 0

    # Iterate over each ingredient in the recipe and its quantity
    for item, price in products.items():
        # Check if the ingredient is optional
        if optionals.__contains__(item):
            # If it is, skip to the next iteration
            continue
        else:
            # If it's not optional, calculate its price and add it to the total
            # Price is calculated by multiplying the price per unit by the quantity used (in percentage)
            # and dividing by 100 (since price is given in cents)
            total_price += prices.get(item) * price / 100

    # Return the total price as an integer (rounded down)
    return int(total_price)
