import requests
import json

# request, response test example
target = "https://jsonplaceholder.typicode.com/users/"
response = requests.get(url=target)
print('response.text: ', response.text[0:100])

# json data sample
json_data = response.json()
print('len(json_data): ', len(json_data))
json_user_1 = json.dumps(json_data[0])
print('json_user_1: ', json_user_1)

# json Obj -> write on file.
with open("./devlopingCodeTest/user.json", "w", encoding="utf-8") as file:
  json.dump(json_user_1, file)
  print('write done.')

# json Arr -> 이름만 모아서 반환.
names = [user["name"] for user in json_data]
print(names)
