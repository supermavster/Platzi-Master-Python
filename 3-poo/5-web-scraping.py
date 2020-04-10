# ¿Qué es web scraping?
# Un web scraping es una herramienta que permite visitar sitios web, analizar su contenido y obtener información.

# Automatizar el analisis de un sitio

import requests
from bs4 import BeautifulSoup
import  urllib

def run():
    for i in range(1,100):
        response = requests.get("https://xkcd.com/{}".format(i))
        soup = BeautifulSoup(response.content, 'html')
        imageContainer = soup.find(id='comic')

        imageUrl = imageContainer.find('img')['src']
        imageName = imageUrl.split('/')[-1]
        print('Downloanding the image {}'.format(imageName))
        urllib.urlretrieve('https://{}'.format(imageUrl), imageName)



if __name__ == "__main__":
    run()