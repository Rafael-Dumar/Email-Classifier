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
    productive_labels = [
        "solicitações de suporte técnico",
        "pedido de atualização sobre um caso em aberto",
        "dúvidas sobre o sistema",
        "email que requer uma ação ou resposta específica"
    ]
    
    unproductive_labels = [
        "mensagens de felicitações",
        "agradecimentos",
        "conversa casual que não necessita de ação",
        "email informativo que não precisa de resposta"
    ]

    all_labels = productive_labels + unproductive_labels

    result = classifier(cleaned_text, candidate_labels=all_labels)
    label = result['labels'][0]
    if label in productive_labels:
        return 'produtivo'
    elif label in unproductive_labels:
        return 'improdutivo'

# Função para gerar resposta com base na classificação
def generate_response(category):
    if category == "produtivo":
        return "Prezado(a), agradecemos seu contato. Recebemos sua solicitação e nossa equipe já está analisando o caso. Retornaremos assim que possível."
    elif category == "improdutivo":
        return "Agradecemos o contato e sua mensagem. Tenha um ótimo dia!"
    else:
        return "Não foi possível determinar uma resposta apropriada."


