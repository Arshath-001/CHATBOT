print("Hello, I am your chatbot . Type 'bye' to exit.")

while True:
    user_input = input("you : ").lower()

    if user_input == "hello" or user_input== "hi":
        print("Bot : Hi there! , How are you?")

    elif user_input == " i am  fine ,you":
        print("Bot : i am just a program, but i am doing Great! , Thanks for asking.")

    elif user_input == "what is your name ?" :
        print("Bot : i am chatbot") 

    elif user_input == "bye":
        print("Bot : goodbye , Have a Nice day") 
        break
    else:
        print("Bot : Sorry , I don't Understand that")         