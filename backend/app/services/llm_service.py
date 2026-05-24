import requests

OLLAMA_URL = "http://localhost:11434/api/generate"

MODEL_NAME = "mistral"


def generate_response(prompt):

    print("Sending prompt to Ollama...")

    response = requests.post(
        OLLAMA_URL,
        json={
            "model": MODEL_NAME,
            "prompt": prompt,
            "stream": False
        }
    )

    print("Received response from Ollama")

    data = response.json()

    return data["response"]