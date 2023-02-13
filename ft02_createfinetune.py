# tested successfully
import openai
from api_secrets import API_KEY
openai.api_key = API_KEY

res = openai.FineTune.create(
    model="ada",
    suffix="CUP_OPENAI_QA",
    training_file="file-DSFtQNaBFoThmcnP15q0seec")
print(res)