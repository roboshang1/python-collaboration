
#Imports the requests library to make the HTTP requests
import requests

#=================================================================================================================

#Gets most recently updated exchange rate from the ExchangeRate-API
def get_exchange_rate(from_currency, to_currency):
    
    url = f"https://open.er-api.com/v6/latest/{from_currency}"

    #Sends a "get" request to the API
    response = requests.get(url)

    #Checks if the response status code is 200 (indicating a successful response)
    if response.status_code == 200:
        
        #"rates" dictionary from the JSON response is retrieved
        rates = response.json().get("rates")

        #Checks if the target currency exists in the rates dictionary
        if rates and to_currency in rates:
            
            #Exchange rate for the target currency is returned
            return rates[to_currency]
        
        else:
            
            #Error message is printed if currency is not identified
            print(f"Error: currency '{to_currency}' not found")
            
    else:
        
        #Error message is printed if the API request fails
        print("Error getting exchange rates")

    #None is returned if the exchange rate could not be retrieved
    return None

#================================================================================================================

#Function to handle user input and perform currency conversion
def convert_currency():
    
    print("Currency Converter")

    #Prompts user for the base and target currency codes, converting them to uppercase
    from_currency = input("Enter the currency code to convert from: ").upper()
    to_currency = input("Enter the currency code to convert to: ").upper()

    #Tries to convert user input to a float and handles errors if input is invalid
    try:
        amount = float(input("Enter the amount to convert: "))
        
    except ValueError:
        
        #Error is printed if the input is not a valid number
        print("Invalid value, please enter a number")
        
        #Function is exited if the input is invalid
        return  

    #Function is called to get the exchange rate
    rate = get_exchange_rate(from_currency, to_currency)

    #Checks if the exchange rate was retrieved successfully
    if rate is not None:
        
        #Calculates the converted amount
        converted_amount = amount * rate

        #Prints the converted amount
        print(f"{amount} {from_currency} is equal to {converted_amount:.2f} {to_currency}")
        
    else:
        
        #Error message is printed if rate retrieval failed
        print("Conversion failed due to rate fetching issue")  

#=========================================================================================================
#Calls the main function to start the currency converter
convert_currency()
