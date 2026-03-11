import requests

url = "https://datadryad.org/api/v2/search?q=qualitative"

response = requests.get(url)

print(response.status_code)
print(response.text[:500])
