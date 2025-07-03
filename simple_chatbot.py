def chatbot():
    print("Chatbot: Hi! How can I help you today?")
    
    while True:
        user_input = input("You: ").lower().strip()
        
        if user_input == "hello":
            print("Chatbot: Hi!")
        
        elif user_input == "how are you":
            print("Chatbot: I'm fine, thanks!")
        
        elif user_input == "bye":
            print("Chatbot: Goodbye!")
            break
        
        else:
            print("Chatbot: Sorry, I don't understand that.")

# Run the chatbot
chatbot()