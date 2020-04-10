# -*- codign: utf-8 -*-
import os
import requests
from bs4 import BeautifulSoup
import  urllib

def run():
    for i in range(1,5):
        # Request GET
        urlBase = "https://xkcd.com/{}".format(i)
        response = requests.get(urlBase)
        content = response.content # Get Content
        # Format Content
        soup = BeautifulSoup(content, "html.parser")
        imageContainer = soup.find(id='comic')
        imageUrl = imageContainer.find('img')['src']
        imageName = imageUrl.split('/')[-1]

        print('Downloanding the image {}'.format(imageName))
        # Make Folder and set the name of image
        newpath = 'images'
        if not os.path.exists(newpath):
            os.makedirs(newpath)
        folder = "{}/{}".format(newpath,imageName)
        # Download File
        urllib.urlretrieve('https:{}'.format(imageUrl), folder)

if __name__ == "__main__":
    run()