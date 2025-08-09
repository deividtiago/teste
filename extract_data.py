import pandas as pd
import requests
from io import StringIO

url = "https://huggingface.co/datasets/kestra/datasets/raw/main/csv/orders.csv"
response = requests.get(url)
df = pd.read_csv(StringIO(response.text))

df.to_csv("raw_data.csv", index=False)
