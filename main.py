def calculate_total(state, records):
    # Define tax rates
    tax_rates = {'NJ': 0.066, 'PA': 0.06, 'DE': 0}

    # Define tax exemptions
    tax_exempt = {'Wic Eligible food', 'Clothing'}

    # Initialize variables
    subtotal = 0
    tax = 0

    # Compute subtotal
    for record in records:
        if record['type'] not in tax_exempt:
            subtotal += record['price']
        elif record['type'] == 'Clothing' and 'fur' not in record['name'].lower():
            subtotal += record['price']

    # Compute tax
    if state in tax_rates:
        tax = subtotal * tax_rates[state]

    # Compute total
    total = subtotal + tax

    # Return total if > 0, else return 0
    return max(total, 0)


records = [
    {'name': 'Apple', 'type': 'Wic Eligible food', 'price': 0.50},
    {'name': 'T-shirt', 'type': 'Clothing', 'price': 10.00},
    {'name': 'Fur coat', 'type': 'Clothing', 'price': 500.00},
    {'name': 'Book', 'type': 'everything else', 'price': 5.00},
]
state = 'DE'
total = calculate_total(state, records)
print(f'Total charge for state {state}: ${total:.2f}')
