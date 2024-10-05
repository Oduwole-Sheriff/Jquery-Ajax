import requests
import json 

class HusmoDataAPI:
    def __init__(self, base_url, auth_token):
        self.base_url = base_url
        self.auth_token = auth_token
        self.headers = {"Authorization": self.auth_token}

    # Get All Data Transactions
    def get_all_data(self):
        url = f"{self.base_url}api/data/"
        print("GET URL: " + url)
        response = requests.get(url, headers=self.headers)
        json_data = response.json()
        json_str = json.dumps(json_data, indent=4)
        print("JSON GET response body: ", json_str)
        print(".......GET Data IS DONE.......")
        print(".......=====================.......")

    # Get Query Data Transaction
    def get_query_data(self, data_id):
        url = f"{self.base_url}api/data/{data_id}"
        print("GET URL: " + url)
        
        try:
            response = requests.get(url, headers=self.headers)
            response.raise_for_status() 
            json_data = response.json()
            json_str = json.dumps(json_data, indent=4)
            print("JSON GET response body: ", json_str)
        except requests.exceptions.RequestException as e:
            print(f"Request failed: {e}")
        except json.JSONDecodeError:
            print("Error decoding JSON response. Response content:")
            print(response.text)
        print(".......GET QUERY DATA TRANSACTION IS DONE.......")
        print(".......=====================.......")

    # Get Query Airtime Transaction
    def get_query_airtime(self):
        self.get_query_data(11)

    # Get Query Bill Payment
    def query_bill_payment(self, data_id):
        url = f"{self.base_url}api/billpayment/{data_id}"
        print("GET URL: " + url)
        
        try:
            response = requests.get(url, headers=self.headers)
            response.raise_for_status() 
            json_data = response.json()
            json_str = json.dumps(json_data, indent=4)
            print("JSON GET response body: ", json_str)
        except requests.exceptions.RequestException as e:
            print(f"Request failed: {e}")
        except json.JSONDecodeError:
            print("Error decoding JSON response. Response content:")
            print(response.text)
        print(".......GET BILL PAYMENT TRANSACTION IS DONE.......")
        print(".......=====================.......")

    # POST Request
    def post_request(self, data):
        url = f"{self.base_url}api/data/"
        print("POST URL: " + url)
        
        response = requests.post(url, json=data, headers=self.headers)
        print("Actual status code:", response.status_code)
        print("Response content:", response.content)

        try:
            json_data = response.json()
            json_str = json.dumps(json_data, indent=4)
            print("JSON POST response body: ", json_str)
            user_id = json_data.get("id")
            print("User ID ===>", user_id)
            print(".......POST/Buy Data IS DONE.......")
            print(".......=====================.......")
            return user_id
        except json.JSONDecodeError:
            print("Error decoding JSON response. Response content:")
            print(response.text)

        return None

    # POST Buy Airtime
    def buy_airtime(self, data):
        url = f"{self.base_url}api/topup/"
        print("POST URL: " + url)
        
        response = requests.post(url, json=data, headers=self.headers)
        print("Actual status code:", response.status_code)
        print("Response content:", response.content)

        try:
            json_data = response.json()
            json_str = json.dumps(json_data, indent=4)
            print("JSON POST response body: ", json_str)
            user_id = json_data.get("id")
            print("User ID ===>", user_id)
            print(".......POST/Airtime TopUp Is Done.......")
            print(".......=====================.......")
            return user_id
        except json.JSONDecodeError:
            print("Error decoding JSON response. Response content:")
            print(response.text)

        return None

    # POST Buy Electricity
    def buy_electricity(self, data):
        url = f"{self.base_url}api/billpayment/"
        print("POST URL: " + url)

        response = requests.post(url, json=data, headers=self.headers)
        print("Actual status code:", response.status_code)
        print("Response content:", response.content)

        try:
            json_data = response.json()
            json_str = json.dumps(json_data, indent=4)
            print("JSON POST response body: ", json_str)
            user_id = json_data.get("id")
            print("User ID ===>", user_id)
            print(".......POST/Electricity Bill Is Done.......")
            print(".......=====================.......")
            return user_id
        except json.JSONDecodeError:
            print("Error decoding JSON response. Response content:")
            print(response.text)

        return None

if __name__ == "__main__":
    base_url = "https://www.husmodata.com/"
    auth_token = "Token e8598384dd0e952ea861431645f26a9c2f3fcf2a"
    
    api = HusmoDataAPI(base_url, auth_token)
    api.get_all_data()
    api.get_query_data(58)
    api.get_query_airtime()
    api.query_bill_payment(15)

    # data for POST requests
    post_data = {
        "network": 1,
        "mobile_number": "07046799827",
        "plan": 51, 
        "Ported_number": True
    }
    api.post_request(post_data)

    airtime_data = {
        "network": 1,
        "amount": 100,
        "mobile_number": "07046799872",
        "Ported_number": True,
        "airtime_type": "VTU"
    }
    api.buy_airtime(airtime_data)

    electricity_data = {
        "disco_name": 1,
        "amount": 10,
        "meter_number": "11", 
        "MeterType": 100
    }
    api.buy_electricity(electricity_data)

