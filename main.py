from langchain_ollama import OllamaLLM

model = OllamaLLM(model="tinyllama")
response = model.invoke("Generate a code in python to be able to ingest csv data using pyspark")
print(response)