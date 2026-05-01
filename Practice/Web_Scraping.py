import pandas as pd
import requests
import io  # Ye nayi line hai

url = 'https://en.wikipedia.org/wiki/List_of_largest_banks'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}

response = requests.get(url, headers=headers)

# Yaha humne io.StringIO use kiya hai taaki Pandas ise text samjhe, file nahi
data_stream = io.StringIO(response.text)
tables = pd.read_html(data_stream, flavor='bs4')

# Pehli table nikalein
df = tables[0]

# Is baar clean output ke liye sirf pehle 5 rows print karte hain
print("--- Table Found Successfully! ---")
print(df.head())
