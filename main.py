from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()
cliente = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
resposta = cliente.chat.completions.create(
    messages=[
        {
            "role": "system",
            "content": "Liste apenas os nomes dos produtos, sem a descrição."
        },
        {
            "role": "user",
            "content": "Liste 3 produtos de skincare para pele oleosa"
        }
    ],
    model="gpt-4o"
)

print(resposta.choices[0].message.content)