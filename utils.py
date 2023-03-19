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
