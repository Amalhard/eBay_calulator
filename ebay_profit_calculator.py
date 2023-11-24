print('Welcome to this simple eBay profit calculator. it will give you a calculation of your expected ebay profits \n'
      'including deductions for such things as promotion fees and variable selling fees and the 80% reduction in\n'
      'selling fees.')
print()
# Global variables of basic figures
gross_profit = float(input('How much did your item sell for?: '))
selling_fee_percentage = float(input('What percentage is your current variable selling fee?: '))
cost = float(input('What was the cost of the product?: '))
selling_fee = gross_profit / 100 * selling_fee_percentage


# will check for the 80% off variable selling fees and alter the variable selling_fees accordingly
def variable_80_percent():
    while True:
        answer = input('Are you benefiting from 80% off variable selling fees? yes/no: ').lower()
        if answer == 'yes':
            selling_fee = gross_profit / 100 * selling_fee_percentage / 100 * 20

        else:
            break
        return selling_fee



# basic net profit calculator
def net_profit():
    basic_net = gross_profit - selling_fee - cost
    print(f"Your net profit is: {round(basic_net, 3)}")


# net profit calulator with promoted listing.

def promo_net_profit():
    promo_fee = float(input("What percentage did you spend on promotion? if 0, type 0: "))
    promo_cost = (gross_profit / 100) * promo_fee
    promo_net = gross_profit - selling_fee - cost - promo_cost
    print(f"Your net profit including a deduction for promotion is: {round(promo_net, 3)}")#Prints to 2 decimal places


def main():

        variable_80_percent()
        answer = input('Have you used ebay to promote your listing?  ').lower()
        if answer == 'yes':
            promo_net_profit()
        else:
            net_profit()

main()