import requests

OLLAMA_URL = "http://localhost:11434/api/embeddings"

def generate_embeddings(chunks, model):
    
    vectors = []
    
    for chunk in chunks:

        response = requests.post(
            OLLAMA_URL,
            json={
                "model":model,
                "prompt":chunk
            }
        )
        
        data = response.json()

        if "embedding" not in data:
            print("Ollama response error:", data)
            raise Exception("embedding not returned")
        
        vectors.append(data["embedding"])
        
    return vectors    