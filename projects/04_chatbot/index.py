# Simple Chatbot
# ----------------------------------
# Concept: String manipulation, basic NLP concepts, dictionaries.
# ----------------------------------
# pseudocode
# 1. Initialize a dictionary with predefined inputs and responses.
#    Example:
#    {
#        "Hello": "Hi, how can I help you?",
#        "What's your name?": "I'm a chatbot.",
#        ...
#    }

# 2. Start a while loop to keep the conversation going until the user decides to quit.

# 3. Inside the loop:
#    3.1. Prompt the user for input.
#    3.2. Convert the user input to a format that matches the dictionary keys (like making it all lower case).
#    3.3. Check if the user input is in the dictionary keys.
#        3.3.1. If it is, print the corresponding response from the dictionary.
#        3.3.2. If it's not, print a default response like "I didn't understand that. Can you try again?".

# 4. Provide a way for the user to end the conversation (like typing 'quit' or 'bye').
# ----------------------------------


def chatbot():
    responses = {
        "hello": "Hi, how can I help you?",
        "what's your name?": "I'm a chatbot.",
        "how are you?": "I'm an AI, I don't have feelings, but thanks for asking!",
    }

    # Lists of greetings and farewell words
    greetings = ["hi", "hello", "hey"]

    farewells = ["bye", "goodbye", "see you"]

    while True:
        # 3.1. Prompt the user for input.
        user_input = input("You: ").lower()

        # Check if the user wants to end the conversation
        if user_input in farewells:
            print("Chatbot: Goodbye!")
            break

        # Check if the user input is a greeting
        elif user_input in greetings:
            print("Chatbot: Hello! How can I assist you today?")

        # Check if the user input is a question
        elif user_input.endswith("?"):
            if user_input in responses:
                print("Chatbot: " + responses[user_input])
            else:
                print("Chatbot: I'm sorry, I don't have an answer to that.")

        # Handle unrecognized inputs
        else:
            print("Chatbot: I didn't understand that. Can you try again?")


chatbot()
