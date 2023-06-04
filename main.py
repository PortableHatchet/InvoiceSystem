import sqlite3


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
    charges = []
    try:
        conn = sqlite3.connect('invoice.db')
        c = conn.cursor()
        job_name = input('Job name: ')
        billing_address = input('Billing address: ')
        phone_number = input('Phone number: ')
        charges = create_charge()
        c.execute('''
            INSERT INTO invoices (job_name, billing_address, phone_number)
            VALUES (?,?,?)
        ''', (job_name, billing_address, phone_number))

        invoice_id = c.lastrowid
        
        for charge in charges:
            c.execute("INSERT INTO charges (invoice_id, charge_description, charge_amount) VALUES (?, ?, ?)", (invoice_id, charge[0], charge[1]))

        conn.commit()
        conn.close()
        print('Success')

    except sqlite3.Error as e:
        print("Error creating invoice:", e)

def view_invoices():
    conn = sqlite3.connect('invoice.db')
    c = conn.cursor()
    c.execute('SELECT * FROM invoices')
    rows = c.fetchall()

    for row in rows:
        invoice_id = row[0]
        name = row[1]
        billing_address = row[2]
        phone_number = row[3]
        paid = row[4]
        #ch_desc = row[2]
        #ch_amt = row[3]
        #print(name, description, ch_desc, ch_amt)
        print(f'=============== {name} ===============')
        print(f'Invoice ID: {invoice_id}')
        print()
        print(f'Billing Address: {billing_address}')
        print(f'Phone Number: {phone_number}')
        print()
        print('Charges: ')
        c.execute('SELECT * FROM charges WHERE invoice_id = ?', (invoice_id, ))
        ch_rows = c.fetchall()
        total_bill = 0
        for ch_row in ch_rows:
            ch_desc = ch_row[2]
            ch_amt = ch_row[3]
            print(f'    {ch_desc} - ${ch_amt}')
            total_bill += ch_amt
        print()
        print(f'    Total: ${total_bill}')
        print()
        if paid == True:
            print('Invoice is paid')
        else:
            print('Invoice has not been paid')
        print('=======================================')
        print('')

    conn.close()

def update_invoice():
    conn = sqlite3.connect('invoice.db')
    c = conn.cursor()

    invoice_option = input('Which invoice would you like to update?(Use invoice ID): ')
    c.execute("""
        SELECT * FROM invoices WHERE invoice_id = ?
    """, (invoice_option, ))
    row = c.fetchone()
    invoice_id = row[0]
    name = row[1]
    billing_address = row[2]
    phone_number = row[3]
    paid = row[4]
    #ch_desc = row[2]
    #ch_amt = row[3]
    #print(name, description, ch_desc, ch_amt)
    print(f'=============== {name} ===============')
    print(f'Invoice ID: {invoice_id}')
    print()
    print(f'Billing Address: {billing_address}')
    print(f'Phone Number: {phone_number}')
    print()
    print('Charges: ')
    c.execute('SELECT * FROM charges WHERE invoice_id = ?', (invoice_id, ))
    ch_rows = c.fetchall()
    total_bill = 0
    for ch_row in ch_rows:
        ch_desc = ch_row[2]
        ch_amt = ch_row[3]
        print(f'    {ch_desc} - ${ch_amt}')
        total_bill += ch_amt
        print()
        print(f'    Total: ${total_bill}')
        print()
    if paid == True:
        print('Invoice is paid')
    else:
        print('Invoice has not been paid')
    print('=======================================')
    print('')

    print('What do you want to update?')
    value_to_update = input('1. Name\n2. Billing Address\n3. Phone Number\n4. Pay Status\n')
    
    if value_to_update == '1':
        new_name = input('What is the new job name?: ')
        c.execute("""
            UPDATE invoices
            SET job_name = ?
            WHERE invoice_id = ?
            """, (new_name, invoice_option))
    elif value_to_update == '2':
        new_billing_address = input('What is the new billing address?: ')
        c.execute("""
            UPDATE invoices
            SET billing_address = ?
            WHERE invoice_id = ?
            """, (new_billing_address, invoice_option))
    if value_to_update == '3':
        new_phone = input('What is the new phone number?: ')
        c.execute("""
            UPDATE invoices
            SET phone_number = ?
            WHERE invoice_id = ?
            """, (new_phone, invoice_option))
    if value_to_update == '4':
        pay_status = input('Has the invoice been fulfilled?(y/n): ')
        if pay_status == 'y':
            pay_status = True
            c.execute("""
            UPDATE invoices
            SET paid = ?
            WHERE invoice_id = ?
            """, (pay_status, invoice_option))
    conn.commit()
    conn.close()


def main():
    

    user_input = ''
    while user_input != '5':
        print('==============================')
        print('Invoice Manager:')
        print('1. View Current Invoices')
        print('2. Create New Invoice')
        print('3. Update an Invoice')
        print('4. Invoice History')
        print('5. Exit')
        print('==============================')
        user_input = input()
        if user_input == '1':
            view_invoices()
            input('Press ENTER to continue')
        elif user_input == '2':
            create_invoice()
        elif user_input == '3':
            update_invoice()
        

if __name__ == '__main__':
    main()