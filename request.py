import requests

# Definieren der URL, des Endpunkts und der Anfrageparameter
url = 'https://api.example.com'  # Beispiel-URL
endpoint = '/data'  # Beispiel-Endpunkt
params = {'param1': 'value1', 'param2': 'value2'}  # Beispiel-Anfrageparameter

# Senden des HTTP-Requests
response = requests.get(url + endpoint, params=params)

# Überprüfen der Antwort
if response.status_code == 200:
    data = response.json()
    # Verarbeiten der erhaltenen Daten
    print(data)
else:
    print('Fehler beim Senden des HTTP-Requests:', response.status_code)
