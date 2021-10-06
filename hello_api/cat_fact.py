import requests

try:
    response = requests.get('https://catfact.ninja/fact')

    print(response.status_code)
    response.raise_for_status()
    print(response.text)
    print(response.json())

    data = response.json()

    fact = data['fact']
    print(f'Here is a random cat fact:\n{fact}')

except Exception as e:
    print(e)
    print('There was an error making the request.')