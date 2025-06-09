from flask import Flask, render_template, request, jsonify
import torch
from transformers import T5Tokenizer, T5ForConditionalGeneration
import re


# Set device 
device = torch.device("mps" if torch.backends.mps.is_available() else "cpu")

# load model
model = T5ForConditionalGeneration.from_pretrained("./chatbot_model").to(device)
tokenizer = T5Tokenizer.from_pretrained("./chatbot_model")

# Clean text
def clean_text(text):
    text = re.sub(r'\r\n', ' ', text)  
    text = re.sub(r'\s+', ' ', text)   
    text = re.sub(r'<.*?>', '', text)  
    text = text.strip().lower()
    return text

# Chatbot function
def chatbot(query):
    query = clean_text(query)
    input_ids = tokenizer(query, return_tensors='pt', max_length=250, truncation=True)
    inputs = {key: value.to(device) for key, value in input_ids.items()}
    outputs = model.generate(
        inputs["input_ids"],
        max_length=250,
        num_beams=5,
        early_stopping=True
    )
    return tokenizer.decode(outputs[0], skip_special_tokens=True)


app = Flask(__name__)

# Home route to serve the UI
@app.route('/')
def home():
    return render_template('index.html')

# API endpoint to handle chatbot requests
@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json['message']
    response = chatbot(user_input)
    return jsonify({'response': response})

if __name__ == '__main__':
    app.run(debug=True)

