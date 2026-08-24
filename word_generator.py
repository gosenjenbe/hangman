import random
from urllib.request import urlopen

also_not_words = ['CHEWBACCA', 'CAR', 'HOUSE']

not_words = [
    'APPLE',
    'BREAD',
    'CHAIR',
    'DREAM',
    'EARTH',
    'FLAME',
    'GRACE',
    'HEART',
    'IMAGE',
    'JUICE',
    'KNIFE',
    'LIGHT',
    'MUSIC',
    'OCEAN',
    'PLANT',
    'QUEEN',
    'RIVER',
    'SMILE',
    'TRAIN',
    'WATER'
    ]

word_source = "https://www.mit.edu/~ecprice/wordlist.10000"

with urlopen(word_source) as response:
    words = response.read().decode('utf-8').splitlines()

random_word = random.choice(words).upper()

hangman_word = list(random_word)