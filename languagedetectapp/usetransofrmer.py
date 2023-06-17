from transformers import pipeline

model_id = "juliensimon/xlm-v-base-language-id"
p = pipeline("text-classification", model=model_id)
p("Hello world")
# [{'label': 'English', 'score': 0.9802148342132568}]
