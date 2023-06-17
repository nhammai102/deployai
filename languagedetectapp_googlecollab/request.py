import json 
import requests

url = 'https://2b5c-34-142-161-40.ngrok.io/detect'

text = "Chào bạn hiền"

response = requests.get(url, params={'text': text})
result = response.json()

print(result)