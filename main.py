from flask import Flask, render_template
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

@app.route('/')
def index():
    html_page = requests.get("https://thefoxxstuff.bandcamp.com/album/one-soul").content

    soup = BeautifulSoup(html_page, 'html.parser')
    href_profile = [a.get('href') for a in soup.find_all('a', class_='pic')]

    img_profile = [img.get('src').replace('_42.jpg', '_23.jpg') for img in soup.find_all('img', class_='thumb')]
    name_profile = [div.text for div in soup.find_all('div', {'class': 'name'})]


    albums = []
    for i in range(len(name_profile)):
        album = {
            'name': name_profile[i],
            'href': href_profile[i],
            'img': img_profile[i]
        }
        albums.append(album)

    return render_template('index.html', albums=albums)

if __name__ == '__main__':
    app.run(debug=True)