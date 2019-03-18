import requests
import os
from bs4 import BeautifulSoup
import pandas as pd


# img_nums = []
# for i in range(1, 810):
#     img_nums.append('%03d' % i)

# save_dir = 'data/pokedex-images'

# if not os.path.exists(save_dir):
#     os.mkdir(save_dir)

# for i in img_nums:
#     img_data = requests.get('https://assets.pokemon.com/assets/cms2/img/pokedex/full/'+i+'.png').content
#     with open(save_dir+'/'+i+'.png', 'wb') as handler:
#         handler.write(img_data)


def img_from_url(url, file_name, save_dir):
    if not os.path.exists(save_dir):
        os.mkdir(save_dir)
    img_data = requests.get(url).content
    with open(save_dir+'/'+ file_name + '.png', 'wb') as f:
        f.write(img_data)

def html_from_url(url):
    return requests.get(url).text



# soup = BeautifulSoup(html_from_url('https://pokemondb.net/pokedex/national'), 'html.parser')
# images = soup.find_all('span', {'class': 'img-fixed img-sprite'})
# idx = 1
# for im in images:
#     img_from_url(im['data-src'], str('%03d' % idx), '../data/pokemon-mini')
#     idx += 1

soup = BeautifulSoup(html_from_url('https://pokemondb.net/sprites'), 'html.parser')
images = soup.find_all('span', {'class': 'img-fixed icon-pkmn'})
idx = 1
for im in images:
    img_from_url(im['data-src'], str('%03d' % idx), '../data/pokemon-suppermini')
    idx += 1