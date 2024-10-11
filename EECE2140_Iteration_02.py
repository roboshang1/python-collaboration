#EECE2140 Final Project Iteration02
#Zachary Potter + Charles Verity
#Details: very basic currency converter, does not yet have 
#access to live exchange rates for many currencies


#these are in USD to the written currency
exchange_rates = {
    'EUR': 0.94,   
    'GBP': 0.82,   
    'INR': 83.01, 
    'JPY': 149.17, 
    'AUD': 1.55    
}

#simple function to convert USD to the selected currency
def convert_currency(usd_amount, currency_code):
    if currency_code in exchange_rates:
        converted_amount = usd_amount * exchange_rates[currency_code]
        print(f"{usd_amount} USD is {converted_amount:.2f} {currency_code}")
    else:
        print("Invalid currency code, use one of the ones availible")

def main():
    usd_amount = float(input("Enter amount in USD: "))
    currency_code = input("Enter currency to convert to: ").upper()

    convert_currency(usd_amount, currency_code)
    
main()