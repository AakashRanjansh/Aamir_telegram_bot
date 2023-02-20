import requests

TOKEN = "5815767048:AAF4nIm_nHSTnWMYCBzn_8FGwAXPb-BVI7A"
chat_id = "5156263535"


def send(message):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={chat_id}&text={message}"
    requests.get(url).json()

# send("Aakash")