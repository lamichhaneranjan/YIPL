import requests
import random
import json
import string

#base_ul:
base_url="https://gorest.co.in"

#Auth Token:
auth_token="Bearer 4414c726ccebe89bda2a1fee6e9fb147388845171e7df1f7f6749809954faaab"

#get random email id:
def generate_random_email():
    domain="automation.com"
    email_length=10
    random_string = ''.join(random.choice(string.ascii_lowercase) for _ in range(email_length))
    email = random_string + "@" +domain
    return email
#GET Request
def get_request():
    url = base_url+"/public/v2/users/"
    headers = {"Authorization" : auth_token}
    response = requests.get(url, headers=headers)

    json_data = response.json()
    json_str = json.dumps(json_data, indent=4)
    assert response.status_code == 200
    print("json GET respone body:", json_str)
    print("........ GET USER IS DONE ......")
    print("........=================........")

#POST Request
def post_request():
    url = base_url + "/public/v2/users/"
    print("post url:" + url)
    headers = {"Authorization": auth_token}
    data = {
        "name": "Ranjannnn lamichhane",
        "email": generate_random_email(),
        "gender": "male",
        "status": "active"
    }
    response = requests.post(url, json=data, headers=headers)
    print(response.status_code)

    json_data = response.json()
    json_str = json.dumps(json_data, indent=4)
    print("json POST response body: ", json_str)
    user_id = json_data['id']
    assert response.status_code == 201
    assert "name" in json_data
    assert json_data["name"] == "Ranjannnn lamichhane"
    return user_id
    print(".....POST REQUEST IS DONE")
    print("......=====================...........")
    print(" user id ========>" + user_id)


#PUT Request
def put_request(user_id):
    url = base_url + f"/public/v2/users/{user_id}"
    print("PUT url:" + url)
    headers = {"Authorization": auth_token}
    data = {
        "name": "Prabinn lamichhane",
        "email": generate_random_email(),
        "gender": "male",
        "status": "inactive"
    }
    response = requests.put(url, json=data, headers=headers)
    json_data = response.json()
    json_str = json.dumps(json_data, indent=4)
    print("json PUT response body: ", json_str)
    assert response.status_code == 200
    assert json_data['id'] == user_id
    assert json_data['name'] == 'Prabinn lamichhane'
    assert json_data['status'] == 'inactive'


#Delete Request
def delete_request(user_id):
    url = base_url + f"/public/v2/users/{user_id}"
    print("DELETE url: " + url)
    headers = {"Authorization": auth_token}
    response = requests.delete(url, headers=headers)
    assert response.status_code == 204
    print("..... ...DELETE USER ID DONE.......")

get_request()
user_id = post_request()
put_request(user_id)
delete_request(user_id)