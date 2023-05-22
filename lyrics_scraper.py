import re
import requests
from bs4 import BeautifulSoup

# URL of the page to scrape
url = 'https://genius.com/Genius-english-translations-bad-bunny-where-she-goes-english-translation-lyrics'

# Make a GET request to the URL
response = requests.get(url)

# Parse the HTML content of the page with Beautiful Soup
soup = BeautifulSoup(response.content, 'html.parser')

# Find all divs with class "lyrics"
lyrics_divs = soup.find_all('div', {'class': 'Lyrics__Container-sc-1ynbvzw-5 Dzxov'})

# Concatenate the text content of all the divs, adding a line break after each line of text
lyrics = ''
for div in lyrics_divs:
    # Remove square brackets from the div tag
    div = re.sub(r'\[(.*?)\]', '', str(div))
    div = BeautifulSoup(div, 'html.parser')  # Re-parse the modified div tag
    for line in div.stripped_strings:
        lyrics += line + '\n'
    # Remove newlines between parentheses
    lyrics = re.sub(r'\((?:\n\s*)+', '(', lyrics)
    lyrics = re.sub(r'(?:\n\s*)+\)', ')', lyrics)

# Remove any leading/trailing whitespace
lyrics = lyrics.strip()

# Print the lyrics
print(lyrics)
