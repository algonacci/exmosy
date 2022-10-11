from transformers import pipeline, AutoTokenizer, AutoModelForSequenceClassification

pretrained_indo = "StevenLimcorn/indonesian-roberta-base-emotion-classifier"

pretrained_english = AutoModelForSequenceClassification.from_pretrained(
    "bergum/xtremedistil-l6-h384-go-emotion")
english_tokenizer = AutoTokenizer.from_pretrained(
    "bergum/xtremedistil-l6-h384-go-emotion")

nlp_indo = pipeline(
    "sentiment-analysis",
    model=pretrained_indo,
    tokenizer=pretrained_indo
)

nlp_english = pipeline(
    "text-classification",
    model=pretrained_english,
    tokenizer=english_tokenizer
)


def recognize_indo(text):
    processed = nlp_indo(text)
    label = processed[0].get("label")
    score = round(processed[0].get("score"), 2)
    return label, score


def recognize_english(text):
    processed = nlp_english(text)
    label = processed[0].get("label")
    score = round(processed[0].get("score"), 2)
    return label, score
