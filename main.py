

def create_charge():
    next_item = ''
    charges = []
    while next_item != '2':
        print('1. Add a charge')
        print('2. Continue')
        next_item = input()
        if next_item == '1':
            charge_description = input('Charge description: ')
            charge_amount = input('Amount (in $): ')
            charge = [charge_description, charge_amount]
            charges.append(charge)
    return charges


def create_invoice():
    job_name = input('Job name: ')
    description = input('Description: ')
    invoice_charges = create_charge()
    







def main():
    print('==============================')
    print('Invoice Manager:')
    print('1. View Current Invoices')
    print('2. Create New Invoice')
    print('3. Update an Invoice')
    print('4. Invoice History')
    print('==============================')

    user_input = ''
    user_input = input()
    if user_input == '2':
        create_invoice()

if __name__ == '__main__':
    main()