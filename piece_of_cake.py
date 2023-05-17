def get_recipe_price(prices, optionals=[], **products):
    """
        Calculates the total price of a recipe based on ingredient prices and quantities.

        Args:
            prices (dict): A dictionary mapping ingredient names to their respective prices per unit (in cents).
            optionals (list): A list of optional ingredient names that should be excluded from the price calculation.
            **products: Variable keyword arguments representing the ingredients used in the recipe, where the
                ingredient name is the keyword and the quantity used (in percentage) is the value.

        Returns:
            int: The total price of the recipe, rounded down to the nearest integer (in cents).
    """

    total_price = 0

    for item, price in products.items():
        if optionals.__contains__(item):
            continue
        else:
            total_price += prices.get(item) * price / 100

    return int(total_price)
