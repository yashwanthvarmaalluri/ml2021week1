def currency_converter():
    import requests
    url = "https://currency-exchange.p.rapidapi.com/exchange"

    fromm=input("Enter the currency from which you want to convert : ").upper()
    to=input("Enter the currency to which you want to convert : ").upper()
    amount_to_convert=int(input(f"Enter the amount in {fromm} you want to convert into {to} : "))
    querystring = {"q":"1.0","from":fromm,"to":to}
    headers = {
        'x-rapidapi-host': "currency-exchange.p.rapidapi.com",
        'x-rapidapi-key': "84eab0366dmshd0f50a51d21fd0fp1b7bf6jsn9240fdc5c54d"
        }
    
    response = requests.request("GET", url, headers=headers, params=querystring)
    if(float(response.text)==0.0):
        print()
        print("Please Enter Valid currencies ")
        print()
    else:
        print()
        print(f"{amount_to_convert} {fromm}  = {amount_to_convert * float(response.text)} {to}")
        print()