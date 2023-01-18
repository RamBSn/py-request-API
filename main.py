import requests as rq

url = "https://newsapi.org/v2/everything?q=Microsoft&from=2023-01-01&" \
      "sortBy=publishedAt&apiKey=62c8b135c28245f4b790b9d2f5112cc7"
newsapi_key = "62c8b135c28245f4b790b9d2f5112cc7"
request = rq.get(url)
request_data = request.json()
print(request_data)

# print(json.dumps(request_data, indent=4) )
for articles in request_data["articles"]:
    print(articles['title'])
