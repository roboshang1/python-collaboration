import tkinter as tk 

from tkinter import messagebox 

import requests 

  
#================================================================================================================= 

#function to get the most recently updated exchange rate from the ExchangeRate-API 

def get_exchange_rate(from_currency, to_currency): 

    url = f"https://open.er-api.com/v6/latest/{from_currency}" 

    response = requests.get(url) 

  

    #sees if the API request was successful (the HTTP status code 200 indicates a successful response) 

    if response.status_code == 200: 

        rates = response.json().get("rates") 

        if rates: 

            return rates 

        else: 

            messagebox.showerror("Error", f"Error: no rates available for '{from_currency}'.") 

    else: 

        messagebox.showerror("Error", "Error fetching exchange rates. API availability error") 

    return None 

  

#================================================================================================================= 

#function to get available currency codes 

def get_available_currencies(): 

     

    #gets currencies using USD as the base (USD=1 -> EUR=some multiplier) 

    url = "https://open.er-api.com/v6/latest/USD" 

    response = requests.get(url) 

     

    if response.status_code == 200: 

        rates = response.json().get("rates") 

        if rates: 

            return sorted(rates.keys()) 

    else: 

        messagebox.showerror("Error", "Error fetching currency codes. API availability error") 

    return [] 

  

#================================================================================================================= 

#function to handle user input and perform currency conversion 

def convert_currency(): 

    from_currency = from_currency_var.get().upper() 

    to_currency = to_currency_var.get().upper() 

  

    #tries to convert the user input from the amount entry field to a float 

    try: 

        amount = float(amount_var.get()) 

    except ValueError: 

        messagebox.showerror("Error", "Invalid value, please enter a number.") 

        return   

  

    #gets the exchange rates using the initial and target currency 

    rates = get_exchange_rate(from_currency, to_currency) 

     

    #sees if rates are successfully retrieved and the target currency exists in the rates 

    if rates and to_currency in rates: 

        converted_amount = amount * rates[to_currency] 

        result_var.set(f"{amount} {from_currency} = {converted_amount:.2f} {to_currency}") 

  

        #this allows user to do another conversion while staying in the application 

        another_conversion_button.grid(row=5, column=0, columnspan=2, pady=10) 

    else: 

        result_var.set("Conversion failed. Not valid currency code") 

  

#================================================================================================================= 

#function to reset the conversion screen for another conversion 

def reset_conversion_screen(): 

    from_currency_var.set("") 

    to_currency_var.set("") 

    amount_var.set("") 

    result_var.set("") 

    another_conversion_button.grid_remove() 

  

#================================================================================================================= 

#function to show the home screen 

def show_home_screen(): 

    clear_screen() 

  

    app.config(bg="green") 

  

    #displays the title 

    tk.Label( 

        app, 

        text="Welcome to Currency Converter!", 

        font=("Impact", 24), 

        bg="green", 

        fg="white" 

    ).pack(pady=50) 

  

    #displays the start button 

    tk.Button( 

        app, 

        text="Start!", 

        font=("Arial", 14), 

        command=show_conversion_screen, 

        bg="white", 

        fg="green" 

    ).pack(pady=20) 

  

#================================================================================================================= 

#function to show the currency conversion screen 

def show_conversion_screen(): 

    clear_screen() 

  

    app.config(bg="SystemButtonFace") 

  

    #creates the main frame for conversion inputs and results 

    main_frame = tk.Frame(app) 

    main_frame.pack(side="left", padx=20, pady=20) 

  

    #generates the input fields 

    tk.Label(main_frame, text="Currency to Convert From:").grid(row=0, column=0, padx=10, pady=5) 

    tk.Entry(main_frame, textvariable=from_currency_var).grid(row=0, column=1, padx=10, pady=5) 

  

    tk.Label(main_frame, text="Currency to Convert To:").grid(row=1, column=0, padx=10, pady=5) 

    tk.Entry(main_frame, textvariable=to_currency_var).grid(row=1, column=1, padx=10, pady=5) 

  

    tk.Label(main_frame, text="Amount:").grid(row=2, column=0, padx=10, pady=5) 

    tk.Entry(main_frame, textvariable=amount_var).grid(row=2, column=1, padx=10, pady=5) 

  

    tk.Button(main_frame, text="Convert", command=convert_currency).grid(row=3, column=0, columnspan=2, pady=10) 

  

    #this displays the conversion result 

    tk.Label(main_frame, textvariable=result_var, font=("Impact", 14), fg="red").grid(row=4, column=0, columnspan=2, pady=10) 

  

    #prompts user if they want to do another conversion without closing the application 

    global another_conversion_button 

    another_conversion_button = tk.Button(main_frame, text="Do Another Conversion", font=("Arial", 12), command=reset_conversion_screen) 

    another_conversion_button.grid(row=5, column=0, columnspan=2, pady=10) 

    another_conversion_button.grid_remove() 

  

    #create the side scrolling list for available currency codes 

    #should update with the API meaning when a new currency gets added in the future, it will appear 

    side_frame = tk.Frame(app) 

    side_frame.pack(side="right", padx=20, pady=20) 

  

    tk.Label(side_frame, text="Available Currencies:", font=("Arial", 12)).pack(anchor="w") 

    currency_listbox = tk.Listbox(side_frame, height=20, width=20) 

    currency_listbox.pack(side="left", fill="y") 

  

    scrollbar = tk.Scrollbar(side_frame, orient="vertical", command=currency_listbox.yview) 

    scrollbar.pack(side="right", fill="y") 

  

    currency_listbox.config(yscrollcommand=scrollbar.set) 

  

    #fills the scrolling list box with available currencies 

    available_currencies = get_available_currencies() 

    if available_currencies: 

        for currency in available_currencies: 

            currency_listbox.insert("end", currency) 

    else: 

        currency_listbox.insert("end", "Error fetching currencies") 

  

#================================================================================================================= 

#function to clear the current screen 

def clear_screen(): 

    for widget in app.winfo_children(): 

        widget.destroy() 

  

#================================================================================================================= 

#tkinter setup 

app = tk.Tk() 

app.title("Currency Converter") 

  

#input/result variables 

from_currency_var = tk.StringVar() 

to_currency_var = tk.StringVar() 

amount_var = tk.StringVar() 

result_var = tk.StringVar() 

  

#shows home screen when booted up 

show_home_screen() 

  

#runs the app 

app.mainloop() 