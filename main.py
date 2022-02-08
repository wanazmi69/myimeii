from requests


response = requests.get(
    'https://free.currconv.com/api/v7/convert?q=USD_JPY&compact=ultra&apiKey=9006dcb72b6464e75d5d')
data = response.json()
