import os
import sys
import openai
# import config
from cli import main_menu


openai.api_key = "API_KEY"

messages = []
system_msg = input("Hello! I'm Dr. Walgzbot! Before we start I have to tell you something, ok?\n")
messages.append({"role": "system", "content": system_msg})

print("My name is Dr. Walgzbot but I have no formal medical training! Please consult a real doctor if you have any medical concerns. You can return to the main menu by typing 'menu' at any time! Now go ahead and ask me anything!\n")
while True:
    message = input()
    if message == "quit()":
        break
    if message == "menu":
        main_menu()
    messages.append({"role": "user", "content": message})
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages)
    reply = response["choices"][0]["message"]["content"]
    messages.append({"role": "assistant", "content": reply})
    print("\n" + reply + "\n")
