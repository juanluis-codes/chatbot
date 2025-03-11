from langchain_ollama import OllamaLLM

class Chatbot:
    def __init__(self, model):
        self.model_name = model
        self.model = OllamaLLM(model=model)
        
    def chat(self, message):
        print(message)
        response = self.model.invoke(message)
        return response