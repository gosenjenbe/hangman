import random
from urllib.request import urlopen

word_source = "https://www.mit.edu/~ecprice/wordlist.10000"

with urlopen(word_source) as response:
    words = response.read().decode('utf-8').splitlines()

random_word = random.choice(words).upper()

hangman_word = list(random_word)
