from fastapi import FastAPI
from pydantic import BaseModel
from utils import model_prediction

app = FastAPI()

class TextRequest(BaseModel):
    text: str

class TextResponse(BaseModel):
    original_text: str
    corrected_text: str

@app.post("/predict", response_model=TextResponse)
def predict(request: TextRequest):
    corrected_text = model_prediction(request.text)
    return TextResponse(original_text=request.text, corrected_text=corrected_text)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
