def calculate_total(state, records):
    # Define tax rates
    tax_rates = {'NJ': 0.066, 'PA': 0.06, 'DE': 0}

    # Define tax exemptions
    tax_exempt = {'Wic Eligible food', 'Clothing'}

    # Initialize variables
    subtotal = 0.0
    tax = 0.0

    # Iterate through the items and calculate total and taxable prices
    for item in records:
        if item['type'] in tax_exempt:
            # Item is tax exempt
            subtotal += item['price']
        elif item['type'] == 'Clothing':
            if state == 'PA':
                # Clothing is tax exempt in PA
                subtotal += item['price']
            elif state == 'NJ' and 'Fur' not in item['name']:
                # Clothing is tax exempt in NJ except for fur clothing
                subtotal += item['price']
            else:
                # Clothing is taxable
                tax += item['price']
        else:
            # Item is taxable by default
            tax += item['price']

    # Calculate total price with tax
    if state in tax_rates:
        tax_rate = tax_rates[state]
        subtotal += tax + (taxable_price * tax_rate)

    return round(subtotal, 2)


records = [
    {'name': 'Apple', 'type': 'Wic Eligible food', 'price': 0.50},
    {'name': 'T-shirt', 'type': 'Clothing', 'price': 10.00},
    {'name': 'Sneakers', 'type': 'Clothing', 'price': 50.00},
    {'name': 'Laptop', 'type': 'everything else', 'price': 1000.00},
    {'name': 'Milk', 'type': 'Wic Eligible food', 'price': 3.50},
    {'name': 'Coat', 'type': 'Clothing', 'price': 75.00},
    {'name': 'Book', 'type': 'everything else', 'price': 15.00},
    {'name': 'Fur coat', 'type': 'Clothing', 'price': 200.00},
]

state = 'PA'
total = calculate_total(state, records)
print(f'Total charge for state {state}: ${subtotal:.2f}')
