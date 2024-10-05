import requests
import json
from requests.auth import HTTPBasicAuth
from datetime import datetime as Mdate
import random, uuid


class VTPassAPI():
    def __init__(self, base_url, auth_token, public_key):
        self.base_url = base_url
        self.auth_token = auth_token
        self.public_key = public_key
        self.headers = {
            "Authorization": self.auth_token,
            "Public-Key": self.public_key   
        }

    # WALLET BALANCE
    def get_wallet_balance(self):
        url = f"{self.base_url}/api/balance"
        print("GET URL: " + url) 
        response = requests.get(url, auth=HTTPBasicAuth('oduwolesheriff1212@gmail.com', 'olamilekan1212'))
        json_data = response.json()
        json_str = json.dumps(json_data, indent=4)
        balance = json_data.get("contents", {}).get("balance", 0)
        print("JSON GET response body: ", json_str)
        print("Hello Sheriff, your vtpass SANDOX balance is", balance)
        print(".......=====================.......")

    # BUY AIRTIME
    def buy_airtime(self, data):
        url = f"{self.base_url}/api/pay"
        print("POST URL: " + url)
        
        response = requests.post(url, json=data, auth=HTTPBasicAuth('oduwolesheriff1212@gmail.com', 'olamilekan1212'))
        print("Actual status code:", response.status_code)
        # print("Response content:", response.content)

        try:
            result = json.loads(response.text)
            json_str = json.dumps(result, indent=4)
            print("JSON POST response body: ", json_str)
            transaction_id = result["content"]["transactions"]["transactionId"]
            product_name = result["content"]["transactions"]["product_name"]
            print(f"Hellp Sheriff, you have successfully purchased {product_name} from vtpass, using transation id: {transaction_id}")
            return transaction_id
        except json.JSONDecodeError:
            print("Error decoding JSON response. Response content:")
            print(response.text)

        return None

if __name__ == "__main__":
    base_url = "https://sandbox.vtpass.com"
    auth_token = "Token bf022dac3d2e78d8cd0672a7bf0ee72c"
    public_key = "PK_5909b3dc9c261dcc5ed57424808b4d57936c672a766"

    api = VTPassAPI(base_url, auth_token, public_key)
    api.get_wallet_balance()

    # Data For Post Request
    date_time_format = Mdate.now().strftime("%Y%m%d%H%M%S")

    def create_random_id():
        num = random.randint(1000, 4999)
        num_2 = random.randint(5000, 8000)
        num_3 = random.randint(111, 999) * 2
        return str(num) + str(num_2) + str(num_3) + str(uuid.uuid4())
    
    data = {
        'request_id': str(date_time_format) + create_random_id(),
        "serviceID": "MTN",
        'amount': 100,
        "phone": +23407046799872,
    }
    api.buy_airtime(data)
