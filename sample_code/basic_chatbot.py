from bs4 import BeautifulSoup

def chatbot_response(text):
    responses = {
        'hello': 'Hi there!',
        'how are you': 'I am fine, thank you!',
        'bye': 'Goodbye!'
    }
    
    return responses.get(text.lower(), 'I am sorry I do not understand that.')


# Usage
response = chatbot_response('Hello')
print(response)
