import requests, json

url = "http://localhost:5000/api"
data = json.dumps({
    "county": 133,
    "sex": 1
})
r = requests.post(url, data)

print r.json()