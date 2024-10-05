import requests
import random
import json
import string

#base url:
base_url = "http://127.0.0.1:8000"

#Auth token:
auth_token = "Token edba79d698e523db078c3c36ce3265724bf24845"

#get random email id:
def generate_random_email():
    domain = "automation.com"
    email_length = 10
    random_string = ''.join(random.choice(string.ascii_lowercase) for _ in range(email_length))
    email = random_string + "@" + domain
    return email


#GET Request
def get_request():
    url = base_url + "/api/post/"
    print("get url: " + url)
    headers = {"Authorization": auth_token}
    response = requests.get(url, headers=headers)
    assert response.status_code == 200
    json_data = response.json()
    json_str = json.dumps(json_data, indent=4)
    print("json GET response body: ", json_str)
    print(".......GET USER IS DONE.......")
    print(".......=====================.......")

#POST Request
def post_request():
    url = base_url + "/api/post/"
    print("post url: " + url)
    headers = {"Authorization": auth_token}
    data = {
        "name": "BIG_DEV_W",
        "drink": "GUINESS",
    }
    response = requests.post(url, json=data, headers=headers)
    print("Actual status code:", response.status_code)
    print("Response content:", response.content)
    
    json_data = response.json()
    json_str = json.dumps(json_data, indent=4)
    print("json POST response body: ", json_str)

    if response.status_code != 200:
        print("Failed to create user. Exiting...")
        return None

    user_id = json_data["id"]
    print("user id ===>", user_id)
    assert response.status_code == 200
    assert "name" in json_data
    assert json_data["name"] == "BIG_DEV_W"
    print(".......POST/Create USER IS DONE.......")
    print(".......=====================.......")
    return user_id


#PUT Request
def put_request(user_id):
    url = base_url + "/api/post/"
    print("put url: " + url)
    headers = {"Authorization": auth_token}
    data = {
        "id": user_id,
        "name": "BIG_SHEG",
        "drink": "GUINESS",
    }
    response = requests.put(url, json=data, headers=headers)
    assert response.status_code == 200
    json_data = response.json()
    json_str = json.dumps(json_data, indent=4)
    print("json PUT response body: ", json_str)
    assert json_data["id"] == user_id
    assert json_data["name"] == "BIG_SHEG"
    print(".......PUT/Update USER IS DONE.......")
    print(".......=====================.......")


#DELETE Request
def delete_request(user_id):
    url = base_url + "/api/post/"
    print("DELETE url: " + url)
    headers = {"Authorization": auth_token}
    data = {
        "id": user_id
    }
    response = requests.delete(url, json=data, headers=headers)
    assert response.status_code == 200
    print(".......DELETE USER IS DONE.......")
    print(".......=====================.......")


#call
get_request()
user_id = post_request()
put_request(user_id)
delete_request(user_id)