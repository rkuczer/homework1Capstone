def calculate_total(state, records):
    # Define tax rates
    tax_rates = {'NJ': 0.066, 'PA': 0.06, 'DE': 0}

    # Define tax exemptions
    tax_exempt = {'Wic Eligible food', 'Clothing'}

    # Initialize variables
    total = 0.0
    taxable_total = 0.0
    subtotal = 0.0
    tax_rate = tax_rates[state]

    # Iterate through the items and calculate total and taxable prices
    for item in records:
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


def get_state():
    while True:
        state = input("Enter your state (DE, PA, NJ): ")
        if state in ('DE', 'PA', 'NJ'):
            return state
        print("Invalid state. Please enter DE, PA, or NJ.")


records = [
    {'name': 'Sneakers', 'type': 'Clothing', 'price': 50.00},
    {'name': 'jeans', 'type': 'Clothing', 'price': 75.00},
    {'name': 'Fur coat', 'type': 'Clothing', 'price': 200.00},
    {'name': 'log', 'type': 'everything else', 'price': 100.00},
    {'name': 'apple', 'type': 'Wic Eligible food', 'price': 100.00}
]

run = True
while run:
    state = get_state()
    total_price = calculate_total(state, records)
    print(f'Total charge for state {state}: ${total_price:.2f}')

    user_input = input("Enter 'q' to quit or any other key to continue: ")
    if user_input == "q":
        run = False
        print("Goodbye! Hope you enjoyed my program. ")
