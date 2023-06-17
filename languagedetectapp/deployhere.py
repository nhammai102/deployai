from fastapi import FastAPI
from transformers import pipeline

model_id = "juliensimon/xlm-v-base-language-id"
p = pipeline("text-classification", model=model_id)

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Language Identification API"}

@app.get("/identify/")
async def identify(text: str):
    result = p(text)[0]
    return result 

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)