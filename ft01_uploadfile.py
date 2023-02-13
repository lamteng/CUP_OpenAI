# tested successfully
import os
import openai
from api_secrets import API_KEY
openai.api_key = API_KEY
res = openai.File.create(
  file=open("pubmed1.jsonl", "rb"),
  purpose='fine-tune'
)
print(res)