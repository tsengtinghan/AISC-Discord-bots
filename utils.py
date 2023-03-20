import requests
from bs4 import BeautifulSoup
import openai
from config import OPENAI_API_KEY

openai.api_key = OPENAI_API_KEY

def extract_text_from_url(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    text = ' '.join(map(lambda p: p.text, soup.find_all('p')))
    return text.strip()

async def generate_summary(text):
    prompt = f"Please summarize the following text:\n{text}"
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=100,
        n=1,
        stop=None,
        temperature=0.5,
    )

    summary = response.choices[0].text.strip()
    return summary

async def classify(text):
    prompt = f'Please classify the text into one of the following categories:\
        ai, science, fintech, economics finance, us-college, competitions and hackathons, \
        and career development, you should respond with the exact same words I mentioned and do not add \
        anymore texts to explain: \n{text}'
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=100,
        n=1,
        stop=None,
        temperature=0.5,
    )
    classify_result = response.choices[0].text.strip()
    return classify_result

async def which_channel(result):
    if(result == "us-college")