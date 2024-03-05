import io
import sys

def clean_up_data(string: str, token='”', replace_with=''):
    """Removes close double quotes and strips any empty spaces from supplied string"""
    return string.replace(token, replace_with).lower().strip()

def format_name(string: str):
    return string.lower().capitalize()

def get_customer_invoices(first_name: str, last_name: str):
    """
    Returns customer invoices by first name and last name

        Parameters:
            first_name (string): Customer's first name
            last_name (string): Customer's last name

        Returns:
            a list of dictionaries of customer invoice data
    """
    with io.open('./data/customer.txt', 'r', encoding='utf8') as customer_file:
        lines = customer_file.readlines()
        customer_found = False
        for line in lines:
            line = line.split(',')
            fn = clean_up_data(line[1]).lower().capitalize()
            ln = clean_up_data(line[2]).lower().capitalize()
            if (fn == first_name) and (ln == last_name):
                customer_id = line[0].replace('“', '').replace('”', '')
                customer_found = True
                break
        if not customer_found:
            print(f'[info]\tNo customer named "{first_name} {last_name}" was found')
            exit(0)
    print('[info]\tFound customer', first_name, last_name)        
    print('[info]\tFetching data.....')
    
    customer_invoices = []
    with io.open('./data/invoice.txt','r', encoding='utf8') as invoice_file:
        invoices = invoice_file.readlines()
        invoice_found = False
        for invoice in invoices:
            invoice = invoice.split(',')
            invoice_customer_id = invoice[0].replace('“', '').replace('”', '')
            if invoice_customer_id == customer_id:
                invoice_found = True
                invoice_obj = {}
                invoice_obj['customer_name'] = f'{first_name} {last_name}'
                invoice_obj['customer_id'] = customer_id
                invoice_obj['invoice_id'] = invoice[1].replace('”', '').strip()
                invoice_obj['amount'] = invoice[2].replace('”', '').strip()
                invoice_obj['date'] = invoice[3].replace('”', '').strip()
                customer_invoices.append(invoice_obj)       
    if not invoice_found:    
        print('[info]\tNo invoice(s) were found for', first_name, last_name)
        exit(0)
    return customer_invoices

def append_items_to_invoice(customer_invoices: list):
    """
    append item data related to customer invoice

        Parameters:
            customer_invoice (list): a list of dictionaries of customer invoice data

        Returns:
            a list of dictionaries of customer invoice data with item data
    """
    with io.open('./data/item.txt', 'r', encoding='utf8') as item_file:
        items = item_file.readlines()
        for customer_invoice in customer_invoices:
            temp = {}
            for item in items:
                item = item.split(',')
                item_invoice_id = item[0].replace('“', '').replace('”', '')
                if item_invoice_id == customer_invoice['invoice_id']:
                    item_info = {}
                    item_id = item[1].replace('”', '').strip()
                    item_info['item_amount'] = item[2].replace('”', '').strip()
                    item_info['item_quantity'] = item[3].replace('”', '').strip()
                    temp[item_id] = item_info
            customer_invoice['items'] = temp
    return customer_invoices

def print_report(customer_invoices: list):
    """
    Prints customer data to console
        Parameters:
            a list of dictionaries of customer invoice data with item data
        Returns:
            None
    """
    print('------------------------------------------------------------------------')
    print(f'Customer:\t{customer_invoices[0]["customer_name"]}\tID:\t{customer_invoices[0]["customer_id"]}')
    for customer_invoice in customer_invoices:
        print('-----------------------------------------------------------------------\n')
        print(f'Invoice ID:\t{customer_invoice["invoice_id"]}\t{customer_invoice["date"]}\n')
        invoice_total = 0.00
        print(f'\tItem(s)\t\t\tAmount\t\tQty')
        for k, v in customer_invoice['items'].items():
            print(f'\t{k}\t\t{v["item_amount"]}\t\t{v["item_quantity"]}')
            invoice_total = invoice_total + (float(v['item_amount']) * int(v['item_quantity']))
        print(f'\nInvoice Total:\t\t\t\t\t{invoice_total}')

    print('\n----------- END OF REPORT -----------')


if len(sys.argv) == 3:
    first_name = format_name(sys.argv[1])
    last_name = format_name(sys.argv[2])
else:
    print('[error]\tPlease provide first AND last name')
    exit(0)

customer_invoices = get_customer_invoices(first_name, last_name)
customer_invoices = append_items_to_invoice(customer_invoices)
print_report(customer_invoices)
