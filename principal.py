import re
import os
import requests
from dotenv import load_dotenv

load_dotenv()

api_url = "https://api-inference.huggingface.co/models/facebook/bart-large-mnli"
HF_TOKEN = os.getenv('HF_TOKEN')
headers = {"Authorization": f"Bearer {HF_TOKEN}"}

# Função para limpar o texto
def clean_text(text):
    # remove tags html
    text = re.sub(r'<.*?>', '', text)
    #remove whitespace
    text = re.sub(r'\s+', ' ', text).strip()
    return text

# Função para classificar o texto
def classify_text(text):

    all_label = [
        "solicitações de suporte técnico",
        "pedido de atualização sobre um caso em aberto",
        "dúvidas sobre o sistema",
        "relatório de um problema ou erro",
        "pedido de informação sobre um produto",
        "mensagens de felicitações",
        "agradecimentos",
        "conversa casual que não necessita de ação",
        "email puramente informativo que não precisa de resposta"
    ]
    productive_labels = [
        "solicitações de suporte técnico",
        "pedido de atualização sobre um caso em aberto",
        "dúvidas sobre o sistema",
        "relatório de um problema ou erro",
        "pedido de informação sobre um produto"
    ]


    payload = {
        "inputs": text,
        "parameters": {"candidate_labels": all_label},
        "options": {"wait_for_model": True}
    }
    try:
        response = requests.post(api_url, headers=headers, json=payload)

        if response.status_code != 200:
            print(f"Erro na api {response.text}")
            return "indefinido"
        
        result = response.json()
        # Pega o label com a maior pontuação
        label = result['labels'][0]
        score = result['scores'][0]

        
        if label in productive_labels and score > 0.47:
            return 'produtivo'
        else:
            return 'improdutivo'
        
    except requests.exceptions.RequestException as e:
        print(f"erro de conexão com a api {e}")
        return "indefinido"

# Função para gerar resposta com base na classificação
def generate_response(category):
    if category == "produtivo":
        return "Prezado(a), agradecemos seu contato. Recebemos sua solicitação e nossa equipe já está analisando o caso. Retornaremos assim que possível."
    elif category == "improdutivo":
        return "Agradecemos o contato e sua mensagem. Tenha um ótimo dia!"
    else:
        return "Não foi possível determinar uma resposta apropriada."



