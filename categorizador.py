from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()
cliente = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
modelo4o = "gpt-4o"
modelo35turbo = "gpt-3.5-turbo"

def categoriza_produto(produto, lista_categorias):
    
    promp_sistema = f"""
        Você é um categorizador de produtos
        Voce deve assumir as categorias na lista abaixo:
        
        # Lista de categorias validas
        {lista_categorias.split(",")}
        
        # Formato de saida
        Produto: Nome do Produto
        Categoria: apresente a categoria do produto
        
        #Exemplo de saida
        Produto: Sabonete
        Categoria: Higiene Pessoal
        
        """
        
    resposta = cliente.chat.completions.create(
        messages=[
            {
                "role": "system",
                "content": promp_sistema
            },
            {
                "role": "user",
                "content": produto
            }
        ],
        model=modelo4o,
        temperature=0,
        max_tokens=200
    )
    
    return resposta.choices[0].message.content
    
categorias_validas = input("Informe as categorias validas, separando por virgulas: ") 
  
while True:
    produto = input("Digite o nome do produto: ")
    resposta = categoriza_produto(produto, categorias_validas)
    print(resposta)



# para mais de uma resposta
# for contador in range(0, 3):
#     print(resposta.choices[contador].message.content)