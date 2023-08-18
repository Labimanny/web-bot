import requests
import lxml
from bs4 import BeautifulSoup

url = 'https://o2tvseries2.com/Fear-the-Walking-Dead-8/index.html'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36 QIHU 360SE'
}
f = requests.get(url, headers=headers)
movies_list = []
soup = BeautifulSoup(f.content, "lxml")
movies = soup.find('div', {
    'class': 'data_list'}).find_all('a')
num = 0
for anchor in movies:
    urls = anchor['href']
    movies_list.append(urls)
    num += 1

    movie_url = urls
    movie_f = requests.get(movie_url, headers=headers)
    movie_soup = BeautifulSoup(movie_f.content, 'lxml')
    movie_content = movie_soup.find('div', {
        'class': 'data'
    })
    print(num, urls,'\n', 'Movie:' + anchor.string.strip())
    print('Movie info:' + movie_content.text.strip())
