import requests

API_URL = "https://api-inference.huggingface.co/models/papluca/xlm-roberta-base-language-detection"
headers = {"Authorization": "Bearer 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"}

def query(payload):
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.json()

# Read text from file
with open("text.txt", "r", encoding="utf-8") as f:
    text = f.read()

output = query({"inputs": text})  

labels = {
    "ar": 0,
    "bg": 1,
    "de": 2,
    "el": 3,
    "en": 4,
    "es": 5,
    "fr": 6,
    "hi": 7,
    "it": 8, 
    "ja": 9,
    "nl": 10,
    "pl": 11,
    "pt": 12,
    "ru": 13,
    "sw": 14,
    "th": 15,
    "tr": 16,
    "ur": 17,
    "vi": 18,
    "zh": 19
}

languages = [
    "Arabic", "Bulgarian", "German", "Greek", "English", "Spanish", "French",
    "Hindi", "Italian", "Japanese", "Dutch", "Polish", "Portuguese", 
    "Russian", "Swahili", "Thai", "Turkish", "Urdu", "Vietnamese", "Chinese" 
]

for lang in output[0]:
    label_idx = labels[lang['label']]
    print(f"{languages[label_idx]}: {lang['score']:.2%}")