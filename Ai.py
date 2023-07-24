import random

def greeting():
    responses = ["Hello!", "Hi!", "Hey there!", "Greetings!"]
    return random.choice(responses)

def farewell():
    responses = ["Goodbye!", "See you later!", "Farewell!", "Have a great day!"]
    return random.choice(responses)

def chatbot_response(user_input):
    user_input = user_input.lower()
    if "hello" in user_input or "hi" in user_input or "hey" in user_input:
        return greeting()
    elif "bye" in user_input or "goodbye" in user_input:
        return farewell()
    else:
        return "I'm just a simple chatbot. I don't understand that yet."

def main():
    print("Chatbot: Hello, I'm your AI chatbot. Type 'bye' to exit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'bye':
            print("Chatbot: Goodbye! Have a great day.")
            break
        response = chatbot_response(user_input)
        print("Chatbot:", response)

if __name__ == "__main__":
    main()
