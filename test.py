import requests
url = "http://localhost:8000/"
customer = {"contract": "two_year", "tenure": 12, "monthlycharges": 10}
requests.post(url, json=customer).json()