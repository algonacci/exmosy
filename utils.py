from transformers import pipeline
pretrained_name = "StevenLimcorn/indonesian-roberta-base-emotion-classifier"

nlp = pipeline(
    "sentiment-analysis",
    model=pretrained_name,
    tokenizer=pretrained_name
)

def recognize(text):
    processed = nlp(text)
    label = processed[0].get("label")
    score = round(processed[0].get("score"), 2)
    return label, score