from transformers import pipeline

classifier = pipeline("zero-shot-classification", model="facebook/bart-large-mnli")

def classifyText(text):
    label = ["produtivo", "improdutivo"]
    result = classifier(text, label)
    return result['labels'][0]

