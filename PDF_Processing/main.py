import requests

# import Pypdf2

url = "https://drive.google.com/drive/u/0/folders/1H9jNq2qKiNOD_pku97UgOOxoxECoDSdb"
filename = "./Example.pdf"

response = requests.get(url)
response.raise_for_status()

with open(filename, "wb") as file:
    file.write(response.content)

print("PDF file downloaded and saved successfully.")