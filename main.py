import chatbot as chat

chatbot = chat.Chatbot("tinyllama")

message = ""
while True:
    message = input("User -> ")
    
    if message == "-1":
        break
    
    print(f"Chat -> {chatbot.chat(message)}")