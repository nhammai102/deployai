import requests

API_URL = "https://api-inference.huggingface.co/models/papluca/xlm-roberta-base-language-detection"
headers = {"Authorization": "Bearer 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"}

def query(payload):
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.json()

# Read text from file
with open("text.txt", "r", encoding="utf-8") as file:
    text = file.read()

output = query({
    "inputs": text,
})

languages = [
    'Arabic', 'Bulgarian', 'German', 'Greek', 'English', 'Spanish', 'French',
    'Hindi', 'Italian', 'Japanese', 'Dutch', 'Polish', 'Portuguese',
    'Russian', 'Swahili', 'Thai', 'Turkish', 'Urdu', 'Vietnamese', 'Chinese'
]

for language in output[0]:
    if language['label'] == 'ar':
        print(f"Arabic: {language['score']:.2%}")
    elif language['label'] == 'bg':
        print(f"Bulgarian: {language['score']:.2%}")
    elif language['label'] == 'de':
        print(f"German: {language['score']:.2%}")
    elif language['label'] == 'el':
        print(f"Greek: {language['score']:.2%}")
    elif language['label'] == 'en':
        print(f"English: {language['score']:.2%}")
    elif language['label'] == 'es':
        print(f"Spanish: {language['score']:.2%}")
    elif language['label'] == 'fr':
        print(f"French: {language['score']:.2%}")
    elif language['label'] == 'hi':
        print(f"Hindi: {language['score']:.2%}")
    elif language['label'] == 'it':
        print(f"Italian: {language['score']:.2%}")
    elif language['label'] == 'ja':
        print(f"Japanese: {language['score']:.2%}")
    elif language['label'] == 'nl':
        print(f"Dutch: {language['score']:.2%}")
    elif language['label'] == 'pl':
        print(f"Polish: {language['score']:.2%}")
    elif language['label'] == 'pt':
        print(f"Portuguese: {language['score']:.2%}")
    elif language['label'] == 'ru':
        print(f"Russian: {language['score']:.2%}")
    elif language['label'] == 'sw':
        print(f"Swahili: {language['score']:.2%}")
    elif language['label'] == 'th':
        print(f"Thai: {language['score']:.2%}")
    elif language['label'] == 'tr':
        print(f"Turkish: {language['score']:.2%}")
    elif language['label'] == 'ur':
        print(f"Urdu: {language['score']:.2%}")
    elif language['label'] == 'vi':
        print(f"Vietnamese: {language['score']:.2%}")
    elif language['label'] == 'zh':
        print(f"Chinese: {language['score']:.2%}")
