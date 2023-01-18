import requests

url = 'https://upload.wikimedia.org/wikipedia/commons/thumb/9/99/Peloneustes_philarchus_Tubingen.JPG/247px-Peloneustes_philarchus_Tubingen.JPG'

response = requests.get(url)

with open('image.jpg', 'wb') as file:
    file.write(response.content)
