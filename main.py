import requests as rq
import smtplib as smtp, ssl
import os


def send_mail(message):
    host = "smtp.gmail.com"
    port = 465
    username = "ramesh.b.sn@gmail.com"
    password = os.getenv("GMAILPASS")

    receiver = "ramesh.b.sn+python@gmail.com"
    sub = "Subject: Python Subject"
    message
    #     = """
    # Python Hi!
    # This is a test meail
    # from python app
    #
    # regards
    # """
    context = ssl.create_default_context()

    with smtp.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)

topic = 'Microsoft'
url = "https://newsapi.org/v2/everything?" \
      f"q={topic}&" \
      "from=2023-01-01&" \
      "sortBy=publishedAt&" \
      "apiKey=62c8b135c28245f4b790b9d2f5112cc7&" \
      "language=en"
newsapi_key = "62c8b135c28245f4b790b9d2f5112cc7"
request = rq.get(url)
request_data = request.json()
print(request_data)

message = ''
# print(json.dumps(request_data, indent=4) )
for article in request_data["articles"][:20]:
    message += article['title'] + '\n' + f'Source: {article["source"]["Name"]}' + '\n' + article['url'] + 2*'\n'

message = "Subject: Python: Microsoft news email\n" + message
message = message.encode('utf-8').strip()
send_mail(message)
