import requests
from bs4 import BeautifulSoup
import json

# URL страницы
url = 'https://www.scrapethissite.com/pages/simple/'

# Получение содержимого страницы
response = requests.get(url)

# Проверка успешности запроса
if response.status_code != 200:
    raise Exception(f"Ошибка доступа к сайту. Код состояния: {response.status_code}")

# Парсинг содержимого страницы
soup = BeautifulSoup(response.content, 'html.parser')

# Получение данных о странах
countries = soup.select('.country')

# Сбор данных в список
country_data = []
for idx, country in enumerate(countries, start=1):
    name = country.select_one('.country-name').get_text(strip=True)
    capital = country.select_one('.country-capital').get_text(strip=True)
    country_data.append({"country": name, "capital": capital})

# Сохранение данных в data.json
with open('data.json', 'w', encoding='utf-8') as f: 
    json.dump(country_data, f, ensure_ascii=False, indent=4)

# Чтение данных из data.json
with open('data.json', 'r', encoding='utf-8') as f: 
    data = json.load(f)

# Создание файла index.html
with open('index.html', 'w', encoding='utf-8') as file:
    file.write("<html><head><title>Страны и столицы</title></head><body>\n")
    file.write('<h1><p align="center"><a href="https://www.scrapethissite.com/pages/simple/">Страны и столицы</a></p></h1>\n')
    file.write('<body bgcolor="#341b4d">\n')
    file.write('<table cellspacing="4" bordercolor="purple" bgcolor="#9163bf" border="3" align="center">\n')
    file.write("<tr><td>Страна</td><td>Столица</td><td>Номер</td></tr>\n")

    # Запись данных в таблицу
    for i, entry in enumerate(data, start=1):
        file.write(f"<tr><td>{entry['country']}</td><td>{entry['capital']}</td><td>{i}</td></tr>\n")

    file.write("</table>\n")
    file.write("</body></html>\n")

print("HTML-страница 'index.html' успешно создана.")
