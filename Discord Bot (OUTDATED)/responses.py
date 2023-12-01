import random

def handle_response(message) -> str:
        p_message = message.lower() #will automatically lower case user input

        if p_message == 'hello': #bot will reply to any of these statements
            return 'Whats up! '
        if p_message == 'Give me a high five!':
            return '*high five*'
        if p_message == 'roll':
            return str(random.randint(1,20))

        if p_message== '!help': #when user inputs !help
            return 'What can I do?'
