import requests

# Definieren der URL, des Endpunkts und der Daten für den Request
url = 'https://api.example.com'  # Beispiel-URL
endpoint = '/data'  # Beispiel-Endpunkt
data = {'key1': 'value1', 'key2': 'value2'}  # Beispiel-Daten für den Request

# Senden des HTTP-Requests
response = requests.post(url + endpoint, json=data)

# Überprüfen der Antwort
if response.status_code == 200:
    result = response.json()
    # Verarbeiten der erhaltenen Ergebnisse
    if 'success' in result:
        print('Die Anfrage war erfolgreich.')
        # Zugriff auf die Antwortdaten gemäß der Datenbankstruktur und Ihren Anforderungen
        if 'data' in result:
            data = result['data']
            # Verarbeiten der Daten gemäß Ihren spezifischen Anforderungen
            print('Erhaltene Daten:', data)
        else:
            print('Keine Daten in der Antwort.')
    else:
        print('Die Anfrage war nicht erfolgreich.')
else:
    print('Fehler beim Senden des HTTP-Requests:', response.status_code)
