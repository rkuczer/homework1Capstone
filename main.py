def calculate_total(state, records):
    # Define tax rates
    tax_rates = {'NJ': 0.066, 'PA': 0.06, 'DE': 0}

    # Define tax exemptions
    tax_exempt = {'Wic Eligible food', 'Clothing'}

    # Initialize variables
    total = 0.0
    taxable_total = 0.0
    subtotal = 0.0

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
                tax_rate = tax_rates[state]
                taxable_total += tax_rate * item['price']
                subtotal += item['price']
        else:
            # Item is taxable by default
            taxable_total += (tax_rates[state] * item['price'])
    total += (subtotal + taxable_total)

    # Calculate total price with tax
    #if state in tax_rates:
    #    tax_rate = tax_rates[state]
    #    total += tax + (tax * tax_rate)

    return max(total, 0)


records = [
    {'name': 'Sneakers', 'type': 'Clothing', 'price': 50.00},
    {'name': 'Milk', 'type': 'Wic Eligible food', 'price': 5.00},
    {'name': 'Coat', 'type': 'Clothing', 'price': 75.00},
    {'name': 'Book', 'type': 'everything else', 'price': 25.00},
    {'name': 'Fur coat', 'type': 'Clothing', 'price': 200.00},
]

state = 'DE'
total_price = calculate_total(state, records)
print(f'Total charge for state {state}: ${total_price:.2f}')
