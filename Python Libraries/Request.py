import requests

# URL of the public API
url = "https://api.coindesk.com/v1/bpi/currentprice.json"

try:
    # Sending a GET request to the API
    response = requests.get(url)
    response.raise_for_status()  # Raise an error for bad status codes

    # Parsing the JSON response
    data = response.json()

    # Extracting and printing a key piece of information
    bitcoin_price = data['bpi']['USD']['rate']
    print(f"Current Bitcoin price in USD: ${bitcoin_price}")

except requests.exceptions.RequestException as e:
    print(f"An error occurred: {e}")