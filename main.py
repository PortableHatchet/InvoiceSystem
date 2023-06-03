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
            #charge = [charge_description, charge_amount]
            #charges.append(charge)

    return charge_amount, charge_description
    


def create_invoice():
        
    try:
        conn = sqlite3.connect('invoice.db')
        c = conn.cursor()
        job_name = input('Job name: ')
        description = input('Description: ')
        ch_amt, ch_desc = create_charge()
        c.execute('''
            INSERT INTO invoices (job_name, job_description, charge_description, charge_amount)
            VALUES (?,?,?,?)
        ''', (job_name, description, ch_desc, ch_amt))
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
        name = row[0]
        description = row[1]
        ch_desc = row[2]
        ch_amt = row[3]
        print(name, description, ch_desc, ch_amt)

    conn.close()

    







def main():
    print('==============================')
    print('Invoice Manager:')
    print('1. View Current Invoices')
    print('2. Create New Invoice')
    print('3. Update an Invoice')
    print('4. Invoice History')
    print('==============================')

    #user_input = ''
    user_input = input()
    if user_input == '1':
        view_invoices()
    elif user_input == '2':
        create_invoice()
    
    

if __name__ == '__main__':
    main()