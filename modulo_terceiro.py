# pip install requests==2.31.0

print("Módulo Terceiro")
import requests

url = "https://www.example.com"
response = requests.get(url)
print(f"Solicitação HTTP para {url} retornou o status code: {response.status_code}")