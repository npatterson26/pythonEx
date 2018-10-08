import requests
page = requests.get('http://roycesite.com')
contents = page.content
print(contents)
