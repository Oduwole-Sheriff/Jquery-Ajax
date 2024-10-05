import requests
import json

class DataStationAPI():
    def __init__(self, base_url, auth_token):
        self.base_url = base_url
        self.auth_token = auth_token
        self.headers = {"Authorization": self.auth_token}

    # USER MANAGEMENT SERVICE (UMS)

    # GET USERS
    def get_all_user(self):
        url = f"{self.base_url}/api/v1/ums/user/"
        print("GET URL: " + url) 
        response = requests.get(url, headers=self.headers)
        json_data = response.json()
        json_str = json.dumps(json_data, indent=4)
        print("JSON GET response body: ", json_str)
        print(".......GET USERS IS DONE.......")
        print(".......=====================.......")

    # GET REFERRER
    def get_user_referrer(self):
        url = f"{self.base_url}/api/v1/ums/user/referrer/"
        print("GET URL: " + url) 
        response = requests.get(url, headers=self.headers)
        json_data = response.json()
        json_str = json.dumps(json_data, indent=4)
        print("JSON GET response body: ", json_str)
        print(".......GET USERS REFERRER IS DONE.......")
        print(".......=====================.......")

    # GENERAL SERVICE (GNS)

    # GET STATES
    def get_states(self):
        url = f"{self.base_url}/api/v1/gns/state/"
        print("GET URL: " + url) 
        response = requests.get(url, headers=self.headers)
        json_data = response.json()
        json_str = json.dumps(json_data, indent=4)
        print("JSON GET response body: ", json_str)
        print(".......GET STATES IS DONE.......")
        print(".......=====================.......")

    # GET NOTIFICATIONS
    def get_notifications(self):
        url = f"{self.base_url}/api/v1/gns/notifications/"
        print("GET URL: " + url) 
        response = requests.get(url, headers=self.headers)
        json_data = response.json()
        json_str = json.dumps(json_data, indent=4)
        print("JSON GET response body: ", json_str)
        print(".......GET NOTIFICATIONS IS DONE.......")
        print(".......=====================.......")

    # GET NOTIFICATION ID
    def get_notifications_id(self, data_id):
        url = f"{self.base_url}/api/v1/gns/notifications/{data_id}"
        print("GET URL: " + url) 
        response = requests.get(url, headers=self.headers)
        json_data = response.json()
        json_str = json.dumps(json_data, indent=4)
        print("JSON GET response body: ", json_str)
        print(".......GET NOTIFICATION ID IS DONE.......")
        print(".......=====================.......")

    # GET CONFIGURATION
    def get_config(self):
        url = f"{self.base_url}/api/v1/gns/config/"
        print("GET URL: " + url) 
        response = requests.get(url, headers=self.headers)
        json_data = response.json()
        json_str = json.dumps(json_data, indent=4)
        print("JSON GET response body: ", json_str)
        print(".......GET CONFIGURATION IS DONE.......")
        print(".......=====================.......")

    # GET SERVICE
    def get_service(self):
        url = f"{self.base_url}/api/v1/gns/service/"
        print("GET URL: " + url) 
        response = requests.get(url, headers=self.headers)
        json_data = response.json()
        json_str = json.dumps(json_data, indent=4)
        print("JSON GET response body: ", json_str)
        print(".......GET SERVICE IS DONE.......")
        print(".......=====================.......")

    # GET SERVICE ID
    def get_service_id(self, data_id):
        url = f"{self.base_url}/api/v1/gns/service/{data_id}"
        print("GET URL: " + url) 
        response = requests.get(url, headers=self.headers)
        json_data = response.json()
        json_str = json.dumps(json_data, indent=4)
        print("JSON GET response body: ", json_str)
        print(".......GET SERVICE ID IS DONE.......")
        print(".......=====================.......")

    # GET PRODUCT
    def get_product(self):
        url = f"{self.base_url}/api/v1/gns/product/"
        print("GET URL: " + url) 
        response = requests.get(url, headers=self.headers)
        json_data = response.json()
        json_str = json.dumps(json_data, indent=4)
        print("JSON GET response body: ", json_str)
        print(".......GET PRODUCT IS DONE.......")
        print(".......=====================.......")

    # GET FAQS
    def get_faqs(self):
        url = f"{self.base_url}/api/v1/gns/faqs/"
        print("GET URL: " + url) 
        response = requests.get(url, headers=self.headers)
        json_data = response.json()
        json_str = json.dumps(json_data, indent=4)
        print("JSON GET response body: ", json_str)
        print(".......GET FAQS IS DONE.......")
        print(".......=====================.......")

    # GET BENEFICIARY
    def get_beneficiary(self):
        url = f"{self.base_url}/api/v1/gns/beneficiary/"
        print("GET URL: " + url) 
        response = requests.get(url, headers=self.headers)
        json_data = response.json()
        json_str = json.dumps(json_data, indent=4)
        print("JSON GET response body: ", json_str)
        print(".......GET BENEFICIARY IS DONE.......")
        print(".......=====================.......")

    # GET LEVEL
    def get_level(self):
        url = f"{self.base_url}/api/v1/gns/level"
        print("GET URL: " + url) 
        response = requests.get(url, headers=self.headers)
        json_data = response.json()
        json_str = json.dumps(json_data, indent=4)
        print("JSON GET response body: ", json_str)
        print(".......GET LEVEL IS DONE.......")
        print(".......=====================.......")

    # GET VIRTUAL BANKS
    def get_virtual_banks(self):
        url = f"{self.base_url}/api/v1/gns/virtualbanks/"
        print("GET URL: " + url) 
        response = requests.get(url, headers=self.headers)
        json_data = response.json()
        json_str = json.dumps(json_data, indent=4)
        print("JSON GET response body: ", json_str)
        print(".......GET VIRTUAL BANKS IS DONE.......")
        print(".......=====================.......")
    
    # GET VIRTUAL ACCOUNTS
    def get_virtual_accounts(self):
        url = f"{self.base_url}/api/v1/gns/virtualaccounts/"
        print("GET URL: " + url) 
        response = requests.get(url, headers=self.headers)
        json_data = response.json()
        json_str = json.dumps(json_data, indent=4)
        print("JSON GET response body: ", json_str)
        print(".......GET VIRTUAL ACCOUNTS IS DONE.......")
        print(".......=====================.......")


    # PAYMENT SERVICE (PMS)

    # GET TRANSACTIONS
    def get_transactions(self):
        url = f"{self.base_url}/api/v1/pms/transactions/?filter=false"
        print("GET URL: " + url) 
        response = requests.get(url, headers=self.headers)
        json_data = response.json()
        json_str = json.dumps(json_data, indent=4)
        print("JSON GET response body: ", json_str)
        print(".......GET TRANSACTIONS IS DONE.......")
        print(".......=====================.......")

    # GET TRANSACTION ID
    def get_transaction_id(self, data_id):
        url = f"{self.base_url}/api/v1/pms/transactions/{data_id}"
        print("GET URL: " + url) 
        response = requests.get(url, headers=self.headers)
        json_data = response.json()
        json_str = json.dumps(json_data, indent=4)
        print("JSON GET response body: ", json_str)
        print(".......GET TRANSACTION ID IS DONE.......")
        print(".......=====================.......")

    # GET TRANSACTIONs STATISTICS
    def get_transaction_statictics(self):
        url = f"{self.base_url}/api/v1/pms/transactions/statistics/"
        print("GET URL: " + url) 
        response = requests.get(url, headers=self.headers)
        json_data = response.json()
        json_str = json.dumps(json_data, indent=4)
        print("JSON GET response body: ", json_str)
        print(".......GET TRANSACTION STATISTICS IS DONE.......")
        print(".......=====================.......")

    # GET FUNDING BUCKET
    def get_funding_bucket(self):
        url = f"{self.base_url}/api/v1/pms/funding/bucket/"
        print("GET URL: " + url) 
        response = requests.get(url, headers=self.headers)
        json_data = response.json()
        json_str = json.dumps(json_data, indent=4)
        print("JSON GET response body: ", json_str)
        print(".......GET FUNDING BUCKET IS DONE.......")
        print(".......=====================.......")

    # GET FUNDING BANK PAYMENT
    def get_funding_bankpayment(self):
        url = f"{self.base_url}/api/v1/pms/funding/bankpayment/"
        print("GET URL: " + url) 
        response = requests.get(url, headers=self.headers)
        json_data = response.json()
        json_str = json.dumps(json_data, indent=4)
        print("JSON GET response body: ", json_str)
        print(".......GET FUNDING BANK PAYMENT IS DONE.......")
        print(".......=====================.......")

    # GET CABLE PLAN
    def get_cable_plan(self):
        url = f"{self.base_url}/api/v1/pms/cableplan/"
        print("GET URL: " + url) 
        response = requests.get(url, headers=self.headers)
        json_data = response.json()
        json_str = json.dumps(json_data, indent=4)
        print("JSON GET response body: ", json_str)
        print(".......GET CABLE PLAN IS DONE.......")
        print(".......=====================.......")

    # GET PLAN
    def get_plan(self):
        url = f"{self.base_url}/api/v1/pms/plan/"
        print("GET URL: " + url) 
        response = requests.get(url, headers=self.headers)
        json_data = response.json()
        json_str = json.dumps(json_data, indent=4)
        print("JSON GET response body: ", json_str)
        print(".......GET PLAN IS DONE.......")
        print(".......=====================.......")

    # GET BILL
    def get_bill(self):
        url = f"{self.base_url}/api/v1/pms/vas/bill/?meterNumber=1233445&billerName=badoo&amount=1000&meterType=prepaid"
        print("GET URL: " + url) 
        response = requests.get(url, headers=self.headers)
        json_data = response.json()
        json_str = json.dumps(json_data, indent=4)
        print("JSON GET response body: ", json_str)
        print(".......GET BILL IS DONE.......")
        print(".......=====================.......")

    # GET WALLET
    def get_wallet(self):
        url = f"{self.base_url}/api/v1/pms/wallet/"
        print("GET URL: " + url) 
        response = requests.get(url, headers=self.headers)
        json_data = response.json()
        json_str = json.dumps(json_data, indent=4)
        print("JSON GET response body: ", json_str)
        print(".......GET WALLET IS DONE.......")
        print(".......=====================.......")

    # GET PAYMENT GATEWAY
    def get_payment_gateway(self):
        url = f"{self.base_url}/api/v1/pms/paymentGateway/"
        print("GET URL: " + url) 
        response = requests.get(url, headers=self.headers)
        json_data = response.json()
        json_str = json.dumps(json_data, indent=4)
        print("JSON GET response body: ", json_str)
        print(".......GET PAYMENT GATEWAY IS DONE.......")
        print(".......=====================.......")

    # GET INTERNET PLAN
    def get_internet_plan(self):
        url = f"{self.base_url}/api/v1/pms/internetplan/"
        print("GET URL: " + url) 
        response = requests.get(url, headers=self.headers)
        json_data = response.json()
        json_str = json.dumps(json_data, indent=4)
        print("JSON GET response body: ", json_str)
        print(".......GET INTERNET PLAN IS DONE.......")
        print(".......=====================.......")

    # GET DISPUTE
    def get_dispute(self):
        url = f"{self.base_url}/api/v1/pms/dispute/"
        print("GET URL: " + url) 
        response = requests.get(url, headers=self.headers)
        json_data = response.json()
        json_str = json.dumps(json_data, indent=4)
        print("JSON GET response body: ", json_str)
        print(".......GET DISPUTE IS DONE.......")
        print(".......=====================.......")

    # GET DISPUTE ID
    def get_dispute_id(self, data_id):
        url = f"{self.base_url}/api/v1/pms/dispute/{data_id}"
        print("GET URL: " + url) 
        response = requests.get(url, headers=self.headers)
        json_data = response.json()
        json_str = json.dumps(json_data, indent=4)
        print("JSON GET response body: ", json_str)
        print(".......GET DISPUTE ID IS DONE.......")
        print(".......=====================.......")

    # DATA FOR POST REQUEST
    # BUY DATA
    def buy_data(self, data):
        url = f"{self.base_url}/api/v1/pms/vas/data/"
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
            print(".......POST/DATA TopUp Is Done.......")
            print(".......=====================.......")
            return user_id
        except json.JSONDecodeError:
            print("Error decoding JSON response. Response content:")
            print(response.text)

        return None
    
    # BUT AIRTIME
    def buy_airtime(self, data):
        url = f"{self.base_url}/api/v1/pms/vas/topup/"
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
            print(".......POST/DATA TopUp Is Done.......")
            print(".......=====================.......")
            return user_id
        except json.JSONDecodeError:
            print("Error decoding JSON response. Response content:")
            print(response.text)

        return None


if __name__ == "__main__":
    base_url = "https://api.datastation.com.ng"
    auth_token = "Token 10815c3603793bc100436b47c47039e79b1d7bf864d297729b"
    
    api = DataStationAPI(base_url, auth_token)
    api.get_all_user()
    api.get_user_referrer()
    api.get_states()
    api.get_notifications()
    api.get_notifications_id("66f91841d05b8c4e0b8e8059")
    api.get_config()
    api.get_service()
    api.get_service_id("66d1ccc630a43475d74bde4d")
    api.get_product()
    api.get_faqs()
    api.get_beneficiary()
    api.get_level()
    api.get_virtual_banks()
    api.get_virtual_accounts()
    api.get_transactions()
    api.get_transaction_id("66f919e4d05b8c4e0b8e80a6")
    api.get_transaction_statictics()
    api.get_funding_bucket()
    api.get_funding_bankpayment()
    api.get_cable_plan()
    api.get_plan()
    api.get_bill()
    api.get_wallet()
    api.get_payment_gateway()
    api.get_internet_plan()
    api.get_dispute()
    api.get_dispute_id("66f69d3f5dc27dba6531b689")

    # DATA FOR POST REQUEST
    data = {
        "phone": "07046799872",
        "plan": "66e05363ebff0cf0305569bb",
        "wallettype": "wallet",
        "pin": "12345"
    }
    api.buy_data(data)

    # BUY AIRTIME
    airtime = {    
        "product": "66df426dff6bdf0fb9cf5e55",
        "phone": "07046799872",
        "amount": "100",
        "pin": "12345"
    }
    api.buy_airtime(airtime)