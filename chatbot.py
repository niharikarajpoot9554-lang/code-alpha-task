#  basic chatbot program
print("============================")
print("welcomre to my chatbot")
print("type'bye' to end the chat")
print("============================")
while True:
    user=input("you").lower()

    if user=="hello":
        print("bot:Hi! nice to meet you.")
    elif user=="hi":
        print("bot:hello!how are you?")
    elif user== "hoe are you":
        print("i am fine, thanks!what about you?")
    elif user== "i am fine":
        print("bot: that's great to hear!")
    elif user== ("what is your name"):
        print("bot:my name is python chatbot.")
    elif user== "who created you":
        print("bot: i was created using python programming.")
    elif user== "thank you":
        print("bot: you're welcome!")
    elif user== "bye":
        print("bot: Goodbye! have a nice day.")
    else:
        print("bot: sorry, i don't understand that.")                        
