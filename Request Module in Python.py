# Requests is an elegant and simple HTTP library for Python, built for human beings.
import requests
r = requests.get(
    'https://financialmodelingprep.com/api/v3/income-statement/AAPL?apikey=demo')
print(r.text)
print(r.status_code)  # Request was okay means get 200

# Post Requests
url = 'www.facebook.com'
data = {
    "p1": 716234567,
    "p2": "war@123"
}
r2 = requests.post(url=url, data=data)
