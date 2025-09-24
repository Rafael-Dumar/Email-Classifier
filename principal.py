from transformers import pipeline
import re
# Carrega o modelo pré-treinado para classificação zero-shot
classifier = pipeline("zero-shot-classification", model="facebook/bart-large-mnli")
# Carrega o modelo pré-treinado para geração de texto
response_generator = pipeline('text-generation', model="pierreguillou/gpt2-small-portuguese")

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

# Função para gerar resposta
def generate_response(category, email):
    if category == "produtivo":
        prompt = f'O seguinte email foi recebido por nossa equipe de suporte: "{email}"\n\nNossa resposta padrão, agradecendo e informando que o caso está sendo analisado, é:'
    elif category == "improdutivo":
        prompt = f'O email a seguir foi recebido: "{email}"\n\nUma resposta curta e educada de confirmação de recebimento é:'
    else:
        return "Categoria desconhecida."
    
    # Gera a resposta
    result = response_generator(prompt, max_length=len(prompt.split()) + 50, num_return_sequences=1, truncation=True)
    final_response = result[0]['generated_text'].replace(prompt, '').strip()
    return final_response


