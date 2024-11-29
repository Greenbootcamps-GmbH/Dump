import requests

# ids= [0, 1, 2, 3 ]
#
# people_names = []
#
# params = {"place": ids[0]}
#
#
# url = f"http://127.0.0.1:8000/people"
#
#
# response = requests.get(url, params=params)
# if response.status_code == 200:
#     response_json = response.json()
#     resonse_dict = dict(response_json)
#     print(resonse_dict["name"])
#
# else:
#     print("ERROR")





url = "http://127.0.0.1:8000/people"

payload = {"name": "Tim",
           "age": 99,
           "street" : "Test Street",
           "housenumber" : 1,
           "city" : "Test City",
           "country" : "Test Country"
           }

headers = {"Content-Type": "application/json"}

response = requests.post(url, json=payload, headers=headers)

if response.status_code == 201:
    print(response.json())
else:
    print(f"Fehler: {response.status_code}")
















