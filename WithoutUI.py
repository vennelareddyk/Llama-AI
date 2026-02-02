import ollama
model = 'llama3.2:1b'
messages=[{"role":"system","content":"You are a helpful assistant, Be concise."}]
print("Ollama chatbot Started...., Type eixt,bye to leave Type your message below to interact with the bot")
while True:
    user_input = input("You:")
    if user_input.lower() in ['exit','bye']:
        print("Exiting chat, Goodbye!")
        break
    messages.append({"role":"user","content":user_input})
    response = ollama.chat(model=model,messages=messages)
    assitant_reply = response["message"]["content"]
    print("Bot:",assitant_reply)
    messages.append({"role":"assitant","contetn":assitant_reply})
