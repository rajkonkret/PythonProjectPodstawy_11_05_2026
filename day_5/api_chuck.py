import requests

url = "https://api.chucknorris.io/jokes/random"

response = requests.get(url)

data = response.json()
print(data)
# {'categories': [],
# 'created_at': '2020-01-05 13:42:26.194739',
# 'icon_url': 'https://api.chucknorris.io/img/avatar/chuck-norris.png',
# 'id': '60uo3YPmSgindMVnsO3gnA',
# 'updated_at': '2020-01-05 13:42:26.194739',
# 'url': 'https://api.chucknorris.io/jokes/60uo3YPmSgindMVnsO3gnA',
# 'value': "When landing on the moon, Neil Armstrong actually said, 'one small step for man, one giant leap for mankind... and please, Chuck Norris, don't kill me for being the first.'"}

print("Kawał:", data['value'])

icon_url = data['icon_url']
print(icon_url)  # https://api.chucknorris.io/img/avatar/chuck-norris.png

response_img = requests.get(icon_url)

with open('icon.png', "wb") as f:
    f.write(response_img.content)
