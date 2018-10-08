import requests
import json
import base64

api_token = 'ce6a0bbbe185315034f1a9dc061daf6c:api_token'
user_token = 'nathanpatterson26@gmail.com:Sampson0'
b64_user = base64.b64encode(user_token.encode())
b64_auth = base64.b64encode(api_token.encode())
#auth_header = {'api_token': api_token}
auth_header = {'Authorization': 'Basic ' + str(b64_user)}

data = requests.get('https://www.toggl.com/api/v8/me', headers=auth_header)

print(data)
"""
json_data = '{"time_entry":{"description":"python programming","tags":["homework"],"pid":123,"created_with":"python"}}'

data = json.loads(json_data)
print(data)
print(type(data))
print(data["time_entry"]["description"])

new_json_data = json.dumps(data, indent=2)
print(new_json_data)
#test = requests.post(https://www.toggl.com/api/v8/time_entries/start, headers=auth_header)

#print(test)
"""
