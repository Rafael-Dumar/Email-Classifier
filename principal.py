from transformers import pipeline
import re
# Carrega o modelo pré-treinado para classificação zero-shot
classifier = pipeline("zero-shot-classification", model="facebook/bart-large-mnli")

# Função para limpar o texto
def clean_text(text):
    # remove tags html
    text = re.sub(r'<.*?>', '', text)
    #remove whitespace
    text = re.sub(r'\s+', ' ', text).strip()
    return text

# Função para classificar o texto
def classify_text(text):
    cleaned_text = text.lower()
    label = ["produtivo", "improdutivo"]
    result = classifier(cleaned_text, candidate_labels=label)
    return result['labels'][0]

# Função para gerar resposta com base na classificação
def generate_response(category):
    if category == "produtivo":
        return "Prezado(a), agradecemos seu contato. Recebemos sua solicitação e nossa equipe já está analisando o caso. Retornaremos assim que possível."
    elif category == "improdutivo":
        return "Agradecemos o contato e sua mensagem. Tenha um ótimo dia!"
    else:
        return "Não foi possível determinar uma resposta apropriada."


