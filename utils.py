# Load the model and tokenizer
import torch
from transformers import T5Tokenizer, T5ForConditionalGeneration
import logging
logging.basicConfig(level=logging.INFO)

print(torch.__version__)
def load_tokenizer():
    try:
        tokenizer = T5Tokenizer.from_pretrained('Spelling_correction/tokenizer')
        return tokenizer
    except Exception as e:
        f"some error occur {e}"
        return None

def load_model():
    try:
        model = T5ForConditionalGeneration.from_pretrained('Spelling_correction/model')

        return model
    except Exception as e:
        f"Some error occur {e}"
        return None
def model_prediction(text):
    tokenizer=load_tokenizer()
    
    input_ids = tokenizer.encode(text, return_tensors='pt') # Move input_ids to the GPU
    
    model=load_model()
    outputs = model.generate(input_ids, max_length=128)
    corrected_text = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return corrected_text
