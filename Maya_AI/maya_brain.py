import requests

API_URL = "https://api-inference.huggingface.co/models/microsoft/DialoGPT-medium"

HEADERS = {
    "Authorization": "Bearer hf_your_new_token_here"
}

def think(command):

    payload = {
        "inputs": command
    }

    response = requests.post(API_URL, headers=HEADERS, json=payload)

    if response.status_code == 200:
        result = response.json()
        try:
            return result[0]["generated_text"]
        except:
            return "Hmm... I am thinking."
    else:
        return "The AI server is busy right now."