import requests
import json
r = requests.get("https://api.forismatic.com/api/1.0/?method=getQuote&lang=en&format=json&key=435251")
d = json.loads(r.text)
print(r)
print(r.status_code)
print(r.content)
b'{"quoteText":"Build up your weaknesses until they become your strong points. ", "quoteAuthor":"Knute Rockne", "senderName":"", "senderLink":"", "quoteLink":"http://forismatic.com/en/79c116d9a5/"}'
print(d["quoteText"])
