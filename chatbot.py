# We are using here the chatbot example as the input() field in jupyter notebook is a bit tricky to handle.
# We need to import dotenv and alll the other stuff from the .env file.
# Also start the Anthropic client.

from dotenv import load_dotenv
import os
import anthropic

load_dotenv()

client = anthropic.Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))

# First lets open an empty list to store the conversation history.
conversation_history = []

# We will use the "while True" loop to keep the conversation going until the user decides to quit.
while True:
    # Ask the user for a message and add it to the conversation history.
    user_message = input("You: ")

    if user_message.lower() == "quit":
        print("Chatbot: Goodbye!")
        break

    conversation_history.append({"role": "user", "content": user_message})
    
    response = client.messages.create(
        model="claude-3-haiku-20240307",
        max_tokens=500,
        messages=conversation_history
    )

    assistant_message = response.content[0].text

    print(f"Chatbot: {assistant_message}")
    conversation_history.append({"role": "assistant", "content": assistant_message})