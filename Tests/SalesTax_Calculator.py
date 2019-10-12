"""

Tax Calculator - Asks the user to enter a cost and either a country or state tax.
It then returns the tax plus the total cost with tax.

"""

import sys

values = sys.argv[1:]
#item_cost = input('Enter the cost: ')
#state = input('Enter the state of sales: ')
sales_tax = {'AK': 0.00, 'AL': 0.04, 'AR': 0.065, 'AZ': 0.056, 'CA': 0.075, 'CT': 0.0635, 'DE': 0.00, 'GA': 0.04,
             'HI': 0.04166,'ID': 0.06, 'IA': 0.06, 'KS': 0.0615, 'KY': 0.06, 'LN': 0.06, 'ME': 0.055, 'MD': 0.06,
             'MN': 0.06875, 'MS': 0.07, 'MO': 0.00, 'NE': 0.055, 'NJ': 0.07, 'NM': 0.05125, 'NY': 0.04, 'NC': 0.0475,
             'ND': 0.05, 'OH': 0.0575, 'OK': 0.045, 'OR': 0.00, 'RI': 0.0599, 'SC': 0.07, 'SD': 0.06, 'TN': 0.07,
             'TX': 0.0625, 'UT': 0.0595,'VT': 0.053, 'WA': 0.065, 'WV': 0.06,'WI': 0.05, 'WY': 0.04, 'NV': 0.0685,
             'LA': 0.05, 'IL': 0.0625, 'PA': 0.06, 'FL': 0.06, 'MT': 0.069, 'CO': 0.029, 'DC': 0.0575, 'IN': 0.07}
#state = state.upper()

#item_tax = float(item_cost) * sales_tax[state]
#print(item_tax)
#purchase_amount = round(float(item_cost) + float(item_tax), 2)
#print(f'Item price is {item_cost}, sales tax is {round(item_tax, 2)} and Purchase amount {purchase_amount}')

if values != []:
    item_cost = values[0]
    state = values[1]

    item_tax = float(item_cost) * sales_tax[state]
    #print(item_tax)
    purchase_amount = round(float(item_cost) + float(item_tax), 2)
    print(f'Item price is ${item_cost}, sales tax is ${round(item_tax, 2)} and Purchase amount ${purchase_amount}')
else:
    print('Rerun the program from the terminal and enter item_cost and the state of sales.')
