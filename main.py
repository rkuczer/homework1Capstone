def calculate_total(state, records):
    # Define tax rates
    tax_rates = {'NJ': 0.066, 'PA': 0.06, 'DE': 0}

    if not records:
        print("Error: Records list is empty. Exiting.")
        return 0

    # Check if state is valid
    if state not in tax_rates:
        print("Error: Invalid state code. Exiting.")
        return 0


    # Initialize variables
    total = 0.0
    taxable_total = 0.0
    subtotal = 0.0
    tax_rate = tax_rates[state]

    #validate item types
    if any(item['price'] < 0 for item in records) or any(item['price'] == 0 for item in records):
        print("Error: Invalid price found in item records, exiting.")
        return 0


    # Iterate through the items and calculate total and taxable prices
    for item in records:
        #validate item type
        item_type = item.get('type')
        if item_type not in ['everything else', 'Wic Eligible food', 'Clothing']:
            print(f"Error: Invalid item type '{item_type}'. Exiting.")
            return 0

        # clothing
        if item['type'] == 'Clothing':
            if state == 'PA':
                # Clothing is tax exempt in PA
                subtotal += item['price']

            elif state == 'NJ' and 'Fur' not in item['name'] and 'fur' not in item['name']:
                # Clothing is tax exempt in NJ except for fur clothing
                subtotal += item['price']

            else:
                # Clothing is taxable
                taxable_total += (tax_rate * item['price'])
                subtotal += item['price']

        # WIC Eligible food
        elif item['type'] == 'Wic Eligible food':
            subtotal += item['price']

        # everything else
        else:
            # Item is taxable by default
            taxable_total += (tax_rates[state] * item['price'])
            subtotal += item['price']

    # calculate total
    total += (subtotal + taxable_total)
    return max(total, 0)


# store inventory for sale
records = [
    {'name': 'Sneakers', 'type': 'Clothing', 'price': 10.00},
    {'name': 'jeans', 'type': 'Clothing', 'price': 75.00},
    {'name': 'Fur coat', 'type': 'Clothing', 'price': 200.00},
    {'name': 'log', 'type': 'everything else', 'price': 100.00},
    {'name': 'apple', 'type': 'Wic Eligible food', 'price': 100.00}
]

#testing code
state = 'PA'
total_charge = calculate_total(state, records)
print(f'Total charge for state {state}: ${total_charge:.2f}')

